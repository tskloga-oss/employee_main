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
```



###  Features

CRUD-ready employee management structure

Django admin integration

Organized template architecture

SQLite database integration

Clean and user-friendly interface

### Technologies Used

1. Python

2. Django

3. SQLite

4. HTML

5. CSS

