# College Notes Management System

![College Notes](https://example.com/college_notes_logo.png)

This project is a College Notes Management System that allows users to manage academic notes, old question papers, syllabus, and books for different subjects in their respective courses. The system supports CRUD operations and handles file uploads for notes, question papers, and syllabus.

## Features

- Create, Read, Update, and Delete (CRUD) operations for Courses, Subjects, Notes, Question Papers, and Syllabus.
- Upload and manage PDF files for Notes, Question Papers, and Syllabus.
- Organize academic materials based on Courses and Subjects.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/manojkhanal/college-notes-management.git
cd college-notes-management

## Getting started with this boilerplate:
##### (eg. in any Linux distribution, you can follow a similar process in another os also.)

1. Create a project root directory in your local machine
```bash
mkdir <project_name> 
```
2. Clone the project in this <project_name> directory (you can use ssh also)
3. Create your virtual environment, activate that environment and install all the requirements
```bash
pip install -r requirements/dev.txt
``` 
4. collect all static files (if run for the first time it creates the assests folder in <project_name> directory)
```bash
django-admin collectstatic
```
5. create `env.py` inside `<project_name/django_project/config/settings/`. Copy from `env.example.py` for the first time and update settings as your requirements.
6. Remember `<project_name>/django_project` is the directory name from where you will run the server.

### optional:
1. Rename the `django_project` by running following command (from inside of your Django environment):
```bash
django-admin rename_project <new_name_for_django_project>
```

2. run migrations
```bash
django-admin migrate
```

3. create superuser
```bash
django-admin create_superuser
```

API Endpoints:  
    api/courses/: List all courses or create a new course.
    api/courses/<int:pk>/: Retrieve, update, or delete a specific course.
    api/subjects/: List all subjects or create a new subject.
    api/subjects/<int:pk>/: Retrieve, update, or delete a specific subject.
    api/notes/: List all notes or create a new note.
    api/notes/<int:pk>/: Retrieve, update, or delete a specific note.
    api/questionpapers/: List all question papers or create a new question paper.
    api/questionpapers/<int:pk>/: Retrieve, update, or delete a specific question paper.
    api/syllabus/: List all syllabi or create a new syllabus.
    api/syllabus/<int:pk>/: Retrieve, update, or delete a specific syllabus.


Authors
    Manoj Khanal
    Email: manojkhanal936@gmail.com

License
    This project is licensed under the MIT License.

## Folder Structure

```
<project_name>
|
|---assets (folder created once static files are collected)
|
|---django_project
|   |---apps
|   |   |---core (custom app)
|   |   |   |---v1
|   |   |   |   |---views
|   |   |   |   |---serializers
|   |   |   |   |---urls.py
|   |   |   |   |---<other util files>
|   |   |   |---v2
|   |   |   |---<versions of apis>
|   |   |---...<other apps>...
|   |   |---urls.py
|   |
|   |---config
|   |   |---settings
|   |   |   |---base.py
|   |   |   |---env.py (ignored by git)
|   |   |   |---env.example.py
|   |   |
|   |   |---asgi.py
|   |   |---urls.py
|   |   |---wsgi.py
|   |   |
|   |   |static_files (all static files we use in development)
|   |   |---base (project as a whole specific static files)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |---core (my custom app specific)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |
|   |---templates
|   |   |---core (custom app specific)
|   |   |---<other app specific templates>
|   |   |---base.html (included basics of jquery and bootstrap)
|   |
|   |---.gitignore
|   |---manage.py
|   |---requirements.txt
|
|---media (folder created once items were uploaded)
|---db.sqlite3
```
