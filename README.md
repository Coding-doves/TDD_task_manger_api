
# 🗂️ Task Manager API

A Test Driven (TDD) backend service built with **FastAPI**, **PostgreSQL**, **SQLAlchemy** for creating, listing, and updating tasks; **Pytest**, **request** for testing.

Project goal is implement Test Driven Development.

### List of Test Implemented
- Integration test - Tests both the endpoints and the return values (database query)
- Units test: Tests only the dependencies that draws data from the database (queries the database)
- API test: Tests only the endpoints 

---

## 📦 Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **request**
- **Pytest**
- **Pydantic**

---

## 🛠️ Setup Instructions

### 1. Clone the project

```
git clone https://github.com/Coding-doves/TDD_task_manager_api.git
cd TDD_task_manager_api
````

### 2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env`

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
```

### 6. Start the FastAPI server

```
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for Swagger UI.

---

## 🧪 Running Tests

```
pytest tests
```

By default, it uses a test SQLite DB (`test_tsk.db`).

---

## ✨ Author

**Ada B. Okonkwo**
[LinkedIn](https://linkedin.com/in/ada-okonkwo) | [GitHub](https://github.com/Coding-doves)

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

```
