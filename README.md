# Student Management System

A simple Django project to store and manage student data with PostgreSQL database.

## Features

- Store student information (personal and academic details)
- List, view, add, edit, and delete students
- Admin interface for data management
- Responsive UI using Bootstrap
- PostgreSQL database for data storage

## Prerequisites

- Python 3.x
- PostgreSQL installed and running
- PostgreSQL database created for the project

## PostgreSQL Setup

1. Install PostgreSQL on your system if not already installed
2. Create a new database:
   ```
   CREATE DATABASE student_management;
   ```
3. Create a user (or use the default postgres user)
4. Grant privileges to the user for the database

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student_management
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure database settings in `student_management/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'student_management',
           'USER': 'postgres',  # Change to your PostgreSQL username
           'PASSWORD': 'postgres',  # Change to your PostgreSQL password
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application:
   - Main application: http://127.0.0.1:8000/students/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

- `students/models.py`: Contains the Student model definition
- `students/views.py`: Contains the views for CRUD operations
- `students/forms.py`: Contains the form for student data input
- `students/templates/students/`: Contains HTML templates for the UI
- `students/urls.py`: Contains URL patterns for the app

## Usage

1. Login to the admin interface to manage students data directly
2. Use the main application to:
   - View a list of all students
   - Add new students
   - View detailed information for each student
   - Edit existing student information
   - Delete students

## Model Fields

The Student model includes the following fields:

- `first_name`: Student's first name
- `last_name`: Student's last name
- `email`: Student's email address (unique)
- `date_of_birth`: Student's date of birth
- `registration_number`: Student's registration/ID number (unique)
- `grade`: Student's grade/class
- `address`: Student's address
- `phone_number`: Student's contact number
- `date_joined`: Date when the student joined 