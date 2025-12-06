
``
# 📝 Task Manager API (Flask + JWT + Swagger)

A simple, clean, and well-structured **Task Manager REST API** built using **Flask**, **SQLAlchemy**, **JWT Authentication**, and **OpenAPI (Swagger UI)**.

This API allows users to register, log in, and perform **CRUD operations on tasks** with authentication and authorization.

---

## 🚀 Features

- User Registration & Login (JWT based authentication)
- CRUD for Tasks (Create, Read, Update, Delete)
- Pagination & Filtering (optional)
- SQLite database for easy local development
- Swagger UI documentation (OpenAPI 3.0)
- Clean folder structure
- Production-ready code
- Includes tests (pytest)

---

## 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Flask 3.x |
| Auth     | Flask-JWT-Extended |
| ORM      | SQLAlchemy |
| Docs     | Swagger UI (OpenAPI JSON) |
| DB       | SQLite (default) |
| Tests    | Pytest |

---

## 📁 Project Structure

```

Task_Manager_Backend/
├── app/
│   ├── **init**.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   ├── routes/
│   │   ├── **init**.py
│   │   ├── auth.py
│   │   └── tasks.py
│   └── static/
│       └── openapi.json
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── run.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/Task_Manager_Backend.git
cd Task_Manager_Backend
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup (SQLite)

SQLite is default — **no configuration needed**.

To initialize the DB:

```bash
python run.py
```

The database file `task.db` is automatically created.

---

## ▶️ Run the Application

```bash
python run.py
```

Your API is available at:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

Swagger documentation:

👉 **[http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)**

---

## 📘 Swagger Documentation (OpenAPI)

Swagger UI will automatically load your OpenAPI JSON available at:

```
/static/openapi.json
```

Open in browser:

👉 **[http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)**

Here you can test:

✔ Register
✔ Login
✔ Create Task
✔ Update Task
✔ Delete Task
✔ List Tasks

---

## 🔐 JWT Authentication Guide

### Step 1 — Register User

**POST /auth/register**

Body:

```json
{
  "username": "john",
  "password": "123456",
  "role": "user"
}
```

---

### Step 2 — Login User

**POST /auth/login**

This returns:

```json

{
  "username": "john",
  "password": "123456"
}

```

Copy the `access_token`.

---

### Step 3 — Authorize in Swagger

Click **Authorize** 🔐 → Paste token like:

```
Bearer <YOUR_JWT_TOKEN>
```

✔ No quotes
✔ Must include the word **Bearer**

---

## 🧪 Testing Endpoints

### ✔ Create Task (Requires JWT)

**POST /tasks**

Body:

```json
{
  "title": "My Task",
  "description": "Task details"
}
```

---

### ✔ Get All Tasks

**GET /tasks**

**GET /tasks** **Pagination**
GET /tasks?page=1&limit=5&completed=false


### ✔ Get Single Task

**GET /tasks/1**

---

### ✔ Update Task

**PUT /tasks/1**

Body:

```json
{
  "title": "Updated",
  "description": "Updated desc",
  "completed": true
}
```

---

### ✔ Delete Task

**DELETE /tasks/1**

---

## 🧪 Run Tests

```bash
pytest -v
```

---

## 🛠️ Environment Variables (Optional)

Default values are provided, but you can create a `.env`:

```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

---

## 🤝 Contribution Guidelines

* Fork the repository
* Create a new feature branch
* Submit a PR

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ❤️ Author

**Tabrez**
Task Manager Backend API (Flask)

---


```

---

```
