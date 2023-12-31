# Table Reservations & Menus API

## Description

This is an API that allows registered users to book tables, manage bookings, add
menus, update menus, and access various functionalities through the browsable API provided by Django REST Framework. The project includes two unit tests  in the app directory that ensure the correct behavior of key functionalities and help maintain code quality.

## API endpoints

**Superuser Account:**
You can log in to the admin panel with the following credentials:

- **URL:** /admin
- **Username:** admin
- **Password:** lemon@789!

| Endpoint | Method |
| ------------ | :-----------: |
| /restaurant    |   GET |
| /restaurant/menu     |   GET - POST   |
| /restaurant/menu/id  |   GET - PUT - DELETE   |
| /restaurant/booking/tables     |   GET - POST   |
| /restaurant/bookings/tables/id     |   GET - PUT - DELETE   |
| /auth/token/login    |   POST (Create token) |
| /auth/users    |   GET - POST - [see djoser's documentation](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints)  |


## Development Setup

### Prerequisites

- Python 3.x
- Pipenv: Install using `pip install pipenv`
- MySQL (optional)

_**Note:**_ This project is configured to use MySQL as the database. If
you prefer to use SQLite, follow the steps in _settings.py_.

### Local setup

1. Clone the repo and cd into the project:
   ```
   git clone https://github.com/yeroldsan/lemon-bistro-api.git
   cd lemon-bistro-api
   ```

2. Check out and follow the instructions in the _.env.example_ file.

3. Activate your virtual environment and install packages:
   ```
   pipenv shell
   pipenv install
   ```

4. Read the _**note**_ above this instrucions, and after updating the file run:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server (running by default on **http://localhost:8000**):
   ```
   python manage.py runserver
   ```






