from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Active les CORS pour toutes les routes

# Obtention de la variable d'environnement
DATABASE_URI = os.getenv("DATABASE_URI")

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Création de la classe Task (Tâche)
class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)


# Migrations
try:
    with app.app_context():
        db.create_all()
        db.session.remove()
    print("Tables created successfully")
except Exception as e:
    print("Error creating tables: {0}".format(e))


# Route principale
@app.route("/")
def index():
    return (
        jsonify(
            {
                "message": "I love Python!",
            }
        ),
        200,
    )


# Avoir toutes les tâches
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    task_list = [
        {"id": task.id, "title": task.title, "done": task.done} for task in tasks
    ]

    return jsonify({"tasks": task_list})


# Avoir une tâche à partir de son id
@app.route("/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)

    if task:
        return jsonify(
            {
                "id": task.id,
                "title": task.title,
                "done": task.done,
            }
        )
    else:
        return jsonify({"error": "Tâche non trouvée"}), 404


# Ajouter une nouvelle tâche
@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "La tâche doit avoir un titre"}), 404

    new_task = Task(title=request.json["title"])
    db.session.add(new_task)
    db.session.commit()

    return (
        jsonify(
            {
                "id": new_task.id,
                "title": new_task.title,
                "done": new_task.done,
            }
        ),
        201,
    )


# Modifier une tâche à partir de son id
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if task:
        task.title = request.json.get("title", task.title)
        task.done = request.json.get("done", task.done)
        db.session.commit()

        return jsonify(
            {
                "new_task": {
                    "id": task.id,
                    "title": task.title,
                    "done": task.done,
                }
            }
        )
    else:
        return (
            jsonify(
                {
                    "error": "Tâche non trouvée",
                }
            ),
            404,
        )


# Supprimer une tâche
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify(
            {
                "result": True,
            }
        )
    else:
        return (
            jsonify(
                {
                    "error": "Tâche non trouvée",
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True)