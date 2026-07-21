from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "tasks.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_tasks = [
            ("Buy milk", False),
            ("Study SQL", False),
            ("Walk Dog", True)
        ]

        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            sample_tasks
        )

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "message": "Hello FlyRank"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/tasks")
def get_tasks():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")

    tasks = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(tasks)

@app.route("/tasks/<int:id>")
def get_task(id):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))

    task = cursor.fetchone()

    conn.close()

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(dict(task))

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (data["title"], False)
    )

    conn.commit()

    task_id = cursor.lastrowid

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    conn.close()

    return jsonify({
        "id": row[0],
        "title": row[1],
        "done": bool(row[2])
    }), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)