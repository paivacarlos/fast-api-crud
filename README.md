# FastAPI Tutorial Project

This project is a RESTful API built with FastAPI and PostgreSQL. It includes CRUD operations for managing registers, with data validation and error handling. The API supports creating, reading, updating, and deleting register entries.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Features

- **Create Register**: Create a new register entry
- **Get Register**: Retrieve a specific register by ID
- **Get All Registers**: Retrieve all register entries
- **Update Register**: Update an existing register
- **Delete Register**: Delete a register by ID
- **Health Check**: Verify if the server is online
- **Data Validation**: Validate CPF and other register fields

## Requirements

- Python 3.11+
- PostgreSQL
- pip for package management

## Installation

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/fast-api-tutorial.git
cd fast-api-tutorial
```

2. Create and Activate Virtual Environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set Up Environment Variables:
Create a `.env` file in the project root with the following content:

```env
DATABASE_URL=postgresql://postgre:123456@localhost/postgres
DEV_URL_BASE=http://127.0.0.1:8000
```

Replace the credentials according to your PostgreSQL configuration.

## Usage

To run the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET` `/health-check`: Check if the server is online
- `POST` `/create-register`: Create a new register
- `GET` `/register/{register_id}`: Get a register by ID
- `GET` `/all-registers`: List all registers
- `PUT` `/update-register/{register_id}`: Update a register by ID
- `DELETE` `/delete-register/{register_id}`: Delete a register by ID

## Testing

To run tests using pytest:

```bash
pytest tests/api
```

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── register.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── createRegisterRouter.py
│   │   ├── deleteRegisterRouter.py
│   │   ├── getAllRegistersRouter.py
│   │   ├── getRegisterByIdRouter.py
│   │   ├── updateRegisterRouter.py
│   │   └── user
│   │       ├── __init__.py
│   │       └── createUserRouter.py
│   ├── services
│   │   ├── __init__.py
│   │   └── registerService.py
│   └── database
│       ├── __init__.py
│       ├── auth
│       ├── base.py
│       └── connection.py
├── tests
│   ├── __init__.py
│   ├── test_example.py
│   └── utils
│       ├── __init__.py
│       └── base_url.py
├── requirements.txt
└── .env
```

