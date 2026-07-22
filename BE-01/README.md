# FlyRank Backend 

## Overview

This project is a Task Management REST API built using Flask and SQLite. It supports Create, Read, Update, and Delete (CRUD) operations while storing data in a SQLite database.

## Technologies Used

- Python 3.12
- Flask
- SQLite3

## Features

- Create a new task
- View all tasks
- View a task by ID
- Update an existing task
- Delete a task
- Persistent SQLite database storage

## Project Structure

```
BE-01/
│── app.py
│── tasks.db
│── README.md
```

## Database

Database Name:

```
tasks.db
```

Table:

```
tasks
```

Columns:

- id
- title
- done

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/<id> | Get task by ID |
| POST | /tasks | Create task |
| PUT | /tasks/<id> | Update task |
| DELETE | /tasks/<id> | Delete task |

## Running the Project

Install Flask:

```bash
pip install flask
```

Run:

```bash
python app.py
```

Server:

```
http://127.0.0.1:5000
```

## Example SQL

```sql
SELECT * FROM tasks;
```

```sql
SELECT COUNT(*) FROM tasks;
```

## Author

Akash MP