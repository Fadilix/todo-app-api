# Flask Task API Documentation

This Flask application provides a simple API for managing tasks.

## Table of Contents

1. [Get All Tasks](#1-get-all-tasks)
2. [Get Task by ID](#2-get-task-by-id)
3. [Add New Task](#3-add-new-task)
4. [Update Task](#4-update-task)
5. [Delete Task](#5-delete-task)

---

## 1. Get All Tasks

- **Endpoint:** `/tasks` (GET)
- **Description:** Get a list of all tasks.
- **Sample Response:**
  ```json
  {
      "tasks": [
          {"id": 1, "title": "Task 1", "done": false},
          {"id": 2, "title": "Task 2", "done": true},
          // Additional tasks...
      ]
  }
## 2. Get Task by ID
- **Endpoint:** /task/<int:task_id> (GET)
- **Description:** Get details of a task by its ID.
- **Sample Response:**
    ```json
    {
    "id": 1,
    "title": "Task 1",
    "done": false
    }
- Error response:
  ```json
  {
    "error": "Task not found"
  }  

### 3. Add New Task

- **Endpoint:** `/tasks` (POST)
- **Description:** Add a new task.
- **Request Body:**
  ```json
  {
      "title": "New Task"
  }

## 4. Update Task

- **Endpoint:** `/tasks/<int:task_id>` (PUT)
- **Description:** Update details of a task by its ID.
- **Request Body:**
  ```json
  {
      "title": "Updated Task",
      "done": true
  }
- Error response:
  ```json
  {
    "error": "Task not found"
  }


## 5. Delete Task

- **Endpoint:** `/tasks/<int:task_id>` (DELETE)
- **Description:** Delete a task by its ID.
- **Sample Response:**
  ```json
  {
      "result": true
  }
- Error response:
  ```json
  {
    "error": "Task not found"
  }

