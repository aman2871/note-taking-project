# Simple Note-Taking API

This project is a simple note-taking API built using Django and Django REST Framework. It allows users to create, fetch, query, and update notes.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/aman2871/note-taking-project/tree/main
   ```

2. Navigate to the project directory:

   ```bash
   cd notetakingproject
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

### Database Setup

1. Apply migrations to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/`.

## API Endpoints

- **Create Note:**
  - Endpoint: `POST /notes/`
  - Create a new note by providing a title and body in the request body.

- **Fetch Note by ID:**
  - Endpoint: `GET /notes/<pk>/`
  - Fetch a note by its primary key.

- **Query Notes by Title Substring:**
  - Endpoint: `GET /notes/?title=<substring>`
  - Query notes based on a substring present in the note's title.

- **Update Note:**
  - Endpoint: `PUT /notes/<pk>/`
  - Update the title and body of an existing note identified by its primary key.

## Testing

To run tests, use the following command:

```bash
python manage.py test
```

## Postman Collection

A Postman collection is provided in the repository (`NoteTaking_API.postman_collection.json`). Import it into Postman to test the API endpoints.
