def register(client, username, password, role="user"):
    return client.post("/auth/register", json={"username": username, "password": password, "role": role})

def login(client, username, password):
    return client.post("/auth/login", json={"username": username, "password": password})

def test_register_login_and_task_crud(client):
    rv = register(client, "alice", "pass123", role="user")
    assert rv.status_code == 201

    rv = register(client, "admin", "adminpass", role="admin")
    assert rv.status_code == 201

    # login alice
    rv = login(client, "alice", "pass123")
    assert rv.status_code == 200
    token = rv.get_json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create task
    rv = client.post("/tasks", json={"title": "My Task"}, headers=headers)
    assert rv.status_code == 201
    task = rv.get_json()
    task_id = task["id"]

    # get task
    rv = client.get(f"/tasks/{task_id}")
    assert rv.status_code == 200

    # update task
    rv = client.put(f"/tasks/{task_id}", json={"completed": True}, headers=headers)
    assert rv.status_code == 200
    assert rv.get_json()["completed"] is True

    # admin delete
    rv = login(client, "admin", "adminpass")
    admin_token = rv.get_json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    rv = client.delete(f"/tasks/{task_id}", headers=admin_headers)
    assert rv.status_code == 204

def test_pagination_and_filtering(client):
    register(client, "u1", "p")
    rv = login(client, "u1", "p")
    token = rv.get_json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    for i in range(15):
        client.post("/tasks", json={"title": f"Task {i}", "completed": i % 2 == 0}, headers=headers)

    rv = client.get("/tasks?page=1&per_page=5")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["page"] == 1
    assert data["per_page"] == 5

    rv = client.get("/tasks?completed=true")
    data = rv.get_json()
    for t in data["items"]:
        assert t["completed"] == True
