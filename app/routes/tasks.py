from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Task
from ..schemas import task_to_dict
from ..utils import jwt_required_custom, current_user

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("", methods=["GET"])
def list_tasks():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    completed = request.args.get("completed")
    owner_id = request.args.get("owner_id")

    query = Task.query
    if completed is not None:
        if completed.lower() in ("true", "1", "yes"):
            query = query.filter_by(completed=True)
        else:
            query = query.filter_by(completed=False)
    if owner_id:
        query = query.filter_by(owner_id=owner_id)

    pagination = query.order_by(Task.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    tasks = [task_to_dict(t) for t in pagination.items]

    return jsonify({
        "items": tasks,
        "page": page,
        "per_page": per_page,
        "total": pagination.total,
        "pages": pagination.pages
    }), 200

@tasks_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"msg": "task not found"}), 404
    return jsonify(task_to_dict(task)), 200

@tasks_bp.route("", methods=["POST"])
@jwt_required_custom
def create_task():
    data = request.get_json() or {}
    title = data.get("title")
    description = data.get("description")
    completed = bool(data.get("completed", False))

    if not title:
        return jsonify({"msg": "title is required"}), 400

    user = current_user()
    if not user:
        return jsonify({"msg": "Authentication required"}), 401

    task = Task(title=title, description=description, completed=completed, owner_id=user.id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task_to_dict(task)), 201

@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required_custom
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"msg": "task not found"}), 404

    user = current_user()
    if not user:
        return jsonify({"msg": "Authentication required"}), 401

    if task.owner_id != user.id and not user.is_admin():
        return jsonify({"msg": "Permission denied"}), 403

    data = request.get_json() or {}
    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "completed" in data:
        task.completed = bool(data["completed"])

    db.session.commit()
    return jsonify(task_to_dict(task)), 200

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required_custom
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"msg": "task not found"}), 404

    user = current_user()
    if not user:
        return jsonify({"msg": "Authentication required"}), 401

    if task.owner_id != user.id and not user.is_admin():
        return jsonify({"msg": "Permission denied"}), 403

    db.session.delete(task)
    db.session.commit()
    return "", 204
