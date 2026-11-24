# Vagabond API

A REST API for Root's Vagabond characters built with Python, FastAPI, and Pydantic. Creator Note: This is one of the mini projects to help me understand creating rest api using FastAPI.

## Overview

Vagabond API provides a structured interface for accessing and managing character information from the board game Root.

Clients can retrieve character information, search by name, create custom characters, update existing records, and delete characters using standard HTTP requests.

## Features

- Information on 12 Vagabond characters
- Character search and filtering
- Full CRUD operations
- Path and query parameters
- Pydantic data validation
- Duplicate ID prevention
- HTTP status codes and error handling
- Automatically generated interactive API documentation

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON
- Swagger UI
- Postman

## How It Works

1. A client sends an HTTP request to an API endpoint.
2. FastAPI routes the request to the corresponding Python function.
3. Pydantic validates incoming data when required.
4. The application retrieves or modifies character information.
5. FastAPI returns a JSON response with an appropriate HTTP status code.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/characters` | Retrieve all characters |
| GET | `/characters/{character_id}` | Retrieve a specific character |
| GET | `/characters?name=tinker` | Search characters by name |
| POST | `/characters` | Create a character |
| PUT | `/characters/{character_id}` | Replace a character |
| PATCH | `/characters/{character_id}` | Partially update a character |
| DELETE | `/characters/{character_id}` | Delete a character |

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
fastapi dev main.py
```

Access the API locally:

- API: http://127.0.0.1:8000/characters
- Swagger UI: http://127.0.0.1:8000/docs

## Example Response

```json
{
    "id": 8,
    "name": "Harrier",
    "ability": "Glide",
    "description": "Travels directly to any clearing by exhausting a torch."
}
```

## Project Status

Completed local mini-project demonstrating REST API development, data validation, CRUD operations, and API testing with Swagger UI and Postman.

## Note

This project is intended for educational and portfolio purposes. The API is not publicly hosted or deployed and is designed to run locally.

Data is stored in memory, meaning all changes reset when the server restarts.

This is an unofficial fan project and is not affiliated with Leder Games.
