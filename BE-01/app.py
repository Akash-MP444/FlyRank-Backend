from flask import Flask, jsonify, request

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
        "endpoints": ["/tasks"]
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

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)

    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(debug=True)