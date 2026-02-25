# Employee Management System – Django Project

## 📌 Project Description

The **Employee Management System** is a Django-based web application designed to manage employee records efficiently.  
It allows administrators to:

- Add new employees  
- View employee details  
- Manage employee information  
- Access an admin dashboard  

This project follows Django best practices in terms of template organization and project structure.

---

## 🚀 Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Activate the virtual environment:

>> Windows : venv\Scripts\activate

>> Mac/Linux: source venv/bin/activate

###  Install Dependencies
```
pip install -r requirements.txt
```

If requirements file is not available:
```bash
pip install django
```

### Database Migrations

Apply migrations to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Admin)
python manage.py createsuperuser

Follow the prompts to create an admin account.

### Run the Server
python manage.py runserver

### Access the app at:
```
http://127.0.0.1:8000/
📁 Project Structure
📂 Static & Media Placement
```

Your static/ and media/ folders are placed inside the main project configuration directory:

employee_main/

instead of the root directory.

📂 Template Organization

Templates are organized inside a subfolder for the employee app, which is a best practice to avoid template name conflicts in larger projects.

Example:

templates/
    employee/
        home.html
        add_employee.html
        employee_detail.html
🗄️ Database

Database used: SQLite

Database file located in root directory:

db.sqlite3

SQLite is lightweight and perfect for development purposes.


✅ Features

CRUD-ready employee management structure

Django admin integration

Organized template architecture

SQLite database integration

Clean and user-friendly interface

🛠️ Technologies Used

Python

Django

SQLite

HTML

CSS

