from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify
from .models import User

def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        user = User.query.get(identity)
        if not user or not user.is_admin():
            return jsonify({"msg": "Admin privilege required"}), 403
        return fn(*args, **kwargs)
    return wrapper

def current_user():
    from flask_jwt_extended import get_jwt_identity
    identity = get_jwt_identity()
    if identity is None:
        return None
    return User.query.get(identity)
