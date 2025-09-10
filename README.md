# Web Development and Python Fundamentals Showcase

This repository is a curated collection of projects and code examples demonstrating foundational skills in web development and Python programming. It includes practical examples of HTML structure, modern CSS layouts like Flexbox and Grid, a complete Twitter UI clone, core Python concepts from basic syntax to Object-Oriented Programming, and a functional REST API built with FastAPI.

## Features

-   **Frontend Development**: Practical examples of modern CSS including Flexbox, Grid, animations, and responsive design, culminating in a visually accurate Twitter UI clone.
-   **Python Fundamentals**: A comprehensive set of scripts covering Python's core concepts, including data structures, control flow, functions, error handling, and OOP.
-   **Backend API**: A complete, documented RESTful API for a Todo application built with the high-performance FastAPI framework.

## Technologies Used

| Technology | Description |
| :--- | :--- |
| [Python](https://www.python.org/) | A versatile programming language used for the core logic and the backend API. |
| [FastAPI](https://fastapi.tiangolo.com/) | A modern, high-performance web framework for building APIs with Python. |
| [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) | The standard markup language for creating web pages and web applications. |
| [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) | The stylesheet language used for describing the presentation of web pages. |

## Usage and Project Spotlights

This repository is structured into distinct sections. You can explore each part individually to see different skills in action.

### 1. Frontend Examples (HTML/CSS)

The `html/` and `css/` directories contain a series of files that demonstrate key web development concepts.

#### Twitter UI Clone

A static clone of the Twitter (X) user interface, built with HTML and CSS.

**To view this project:**
Open the `css/twitter-clone/index.html` file in your web browser.

#### CSS Concepts

Explore individual files to see demonstrations of:
-   **Flexbox Layout**: `css/2-flex.html`
-   **Grid Layout & Use-Case**: `css/4-grid.html`, `css/5-grid-use-case.html`
-   **Animations**: `css/3-animations.html`
-   **Responsive Design**: `css/9-responsive-design.html`

### 2. Python Core Concepts

The `python/` directory contains numerous scripts, each focusing on a specific Python feature. You can run them directly from your terminal.

**Example:**
```bash
python python/17_oop.py
```

### 3. Todo API (FastAPI Backend)

The `fastapi/` directory contains a fully functional REST API. The following section provides detailed documentation for its setup and endpoints.

---

# Todo API

## Overview
This is a RESTful API for managing a simple todo list. It is built with Python using the FastAPI framework for high performance and automatic documentation generation.

## Features
- **FastAPI**: Used for building the robust and asynchronous API endpoints.
- **Pydantic**: Handles data validation and serialization to ensure type safety.

## Getting Started
### Installation
1.  Navigate to the API's directory:
    ```bash
    cd fastapi
    ```
2.  Install the required Python packages:
    ```bash
    pip install "fastapi[all]"
    ```
3.  Start the development server:
    ```bash
    uvicorn main:app --reload
    ```
    The API will now be running on `http://127.0.0.1:8000`.

### Environment Variables
No environment variables are required to run this project.

## API Documentation
### Base URL
`http://127.0.0.1:8000`

### Endpoints
#### GET /todos
Retrieves a list of all todo items.

**Request**:
No payload required.

**Response**: `200 OK`
```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  },
  {
    "id": 2,
    "title": "Build an API",
    "completed": true
  }
]
```

**Errors**:
- None

#### POST /todos
Creates a new todo item.

**Request**: `201 Created`
```json
{
  "title": "Document the API"
}
```

**Response**:
```json
{
  "id": 3,
  "title": "Document the API",
  "completed": false
}
```

**Errors**:
- `422 Unprocessable Entity`: If the `title` field is missing or not a string.

#### GET /todos/{todo_id}
Retrieves a single todo item by its ID.

**Request**:
Path parameter `todo_id` (integer).

**Response**: `200 OK`
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

**Errors**:
- `404 Not Found`: If no todo item matches the provided `todo_id`.

#### PATCH /todos/{todo_id}
Updates an existing todo item's title or completion status.

**Request**: `202 Accepted`
Path parameter `todo_id` (integer).
```json
{
  "title": "Learn advanced FastAPI",
  "completed": true
}
```

**Response**:
```json
{
  "id": 1,
  "title": "Learn advanced FastAPI",
  "completed": true
}
```

**Errors**:
- `404 Not Found`: If no todo item matches the provided `todo_id`.
- `422 Unprocessable Entity`: If the payload contains invalid data types.

#### DELETE /todos/{todo_id}
Deletes a todo item by its ID.

**Request**: `204 No Content`
Path parameter `todo_id` (integer).

**Response**:
An empty response with a `204 No Content` status code.

**Errors**:
- None (The operation is idempotent; deleting a non-existent item does not produce an error).

---

## Author

Connect with me on social media!

-   **Twitter**: [@your_twitter_handle](https://twitter.com/your_twitter_handle)
-   **LinkedIn**: [your_linkedin_profile](https://linkedin.com/in/your_linkedin_profile)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://www.npmjs.com/package/dokugen)