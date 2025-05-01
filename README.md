# README.md

## FastAPI Todo App (Clean Architecture)

This project is a cleanly structured **FastAPI** backend for a **Todo API** using **MySQL** as the database. It follows:

- FastAPI + SQLAlchemy
- Repository, Service, Controller layers
- Production-ready structure for cloud/serverless deployment.

---

## 📦 Project Structure

```plaintext
serverless-python/
├── app/
│   ├── api/            # FastAPI routers
│   ├── controllers/    # Controllers (handle API layer)
│   ├── services/       # Business Logic
│   ├── repositories/   # Repositories (DB access)
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── test/           # Unit tests
│   ├── database.py     # DB Session setup
│   ├── env.py          # Environmental variables setup
│   └── main.py         # App startup
├── .env.sample
├── fastapi-gcp-serverless.code-workspace
├── pytest.ini
├── rav.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/fastapi-todo-clean.git
cd fastapi-todo-clean
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=todo_db
```

(Adapt `app/database.py` to use `python-decouple` for loading from `.env` if needed)

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 🚀 API Endpoints

| Method | URL | Description |
|:------|:---|:-----------|
| POST | `/todos/` | Create new todo |
| GET | `/todos/` | List all todos |
| GET | `/todos/{id}` | Retrieve single todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

Access interactive API docs at:

- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📄 License

MIT License.

---

## 💬 Author

- Created by **LakshanRCosta** 🚀
- Inspired by best practices in FastAPI microservice design.

---

## 🛠️ Running with RAV

This project includes a `rav` configuration for managing common tasks. Below are the available scripts:

### 🔧 Scripts

| Script Name | Command |
|:------------|:--------|
| `runserver` | `uvicorn app.main:app --reload` |
| `installs`  | `venv/bin/python -m pip install -r requirements.txt` |
| `test`      | `pytest .` |
| `build`     | `docker build` |
| `push`      | `docker push` |

### 🚀 Usage

Run the following commands using `rav`:

- Start the development server:

    ```bash
    rav run runserver
    ```

- Install dependencies:

    ```bash
    rav run installs
    ```

- Run tests:

    ```bash
    rav run test
    ```

- Build the Docker image:

    ```bash
    rav run build
    ```

- Push the Docker image:

    ```bash
    rav run push
    ```

---
