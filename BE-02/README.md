# FlyRank Backend – BE-02

## Overview
This project is a Task Management REST API built using **Flask** and **SQLite**. It supports Create, Read, Update, and Delete (CRUD) operations with persistent task storage using a SQLite database.

---

## Technologies Used
- Python 3.12
- Flask
- SQLite3

---

## Features
- Create a new task
- View all tasks
- View a task by ID
- Update an existing task
- Delete a task
- Persistent SQLite database storage

---

## Project Structure

```
BE-02/
│── app.py
│── tasks.db
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Database

**Database Name**
```
tasks.db
```

**Table**
```
tasks
```

**Columns**
- id
- title
- done

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/<id> | Get task by ID |
| POST | /tasks | Create task |
| PUT | /tasks/<id> | Update task |
| DELETE | /tasks/<id> | Delete task |

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## Example SQL Queries

```sql
SELECT * FROM tasks;
SELECT COUNT(*) FROM tasks;
```

---

## Author

**Akash MP**
