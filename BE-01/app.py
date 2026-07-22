from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "completed": False
    },
    {
        "id": 2,
        "title": "Build REST API",
        "completed": False
    }
]


@app.route("/")
def home():
    return jsonify({
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)

    return jsonify({
        "error": "Task not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)