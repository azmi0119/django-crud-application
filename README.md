# Django Employee and Department CRUD Application

## 1. Project Overview

This application is built using Django and PostgreSQL to manage departments and employees.

**Features:**
- Department CRUD operations.
- Employee CRUD operations.
- Employee profile photo upload.
- Department selection using a dropdown.
- Hobbies selection using checkboxes.
- Gender selection using radio buttons.
- Age validation between 18 and 100.
- Profile photo size validation (maximum 5 MB).
- Email notification when an employee is created using Mailtrap.

## 2. Technologies Used

- Python
- Django
- PostgreSQL
- Bootstrap
- Pillow
- python-dotenv
- psycopg
- Mailtrap SMTP

## 3. Create a Virtual Environment

Open the project folder in VS Code and create a virtual environment.

```powershell
python -m venv env
```

**Why?** A virtual environment keeps the project's Python dependencies separate from other projects.

Activate the virtual environment:

```powershell
.\env\Scripts\Activate.ps1
```

## 4. Install Required Packages

```powershell
python -m pip install Django Pillow python-dotenv "psycopg[binary]"
```

**Why?**
- Django provides the web framework.
- Pillow supports image uploads.
- python-dotenv loads environment variables.
- psycopg connects Django to PostgreSQL.

Save the installed dependencies:

```powershell
python -m pip freeze > requirements.txt
```

## 5. Create the PostgreSQL Database

Open pgAdmin and execute the following SQL query:

```sql
CREATE DATABASE django_employee_db;
```

**Why?** This creates the database where employee and department records will be stored.

## 6. Configure PostgreSQL in Django

Open `crudproject/settings.py` and configure the database connection.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_employee_db",
        "USER": "postgres",
        "PASSWORD": "your_actual_postgresql_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Replace the password with your actual PostgreSQL password.

**Why?** This connects the Django application to PostgreSQL instead of SQLite.

## 7. Register the Django Application

Add `crudapp` to the `INSTALLED_APPS` list in `crudproject/settings.py`.

```python
INSTALLED_APPS = [
    # Existing Django applications
    "crudapp",
]
```

Keep the other existing Django applications in the list.

**Why?** This allows Django to recognize the application's models, forms, and migrations.

## 8. Create the Database Models

Open `crudapp/models.py` and define two models.

### Department Model

Stores department information, including the department name and description.

### Employee Model

Stores employee details, including:

- Name
- Age
- Email
- Department
- Profile photo
- Hobbies
- Gender

The employee model uses a `ForeignKey` to connect each employee to a department.

**Why?** Models define the structure of the database tables and the relationship between employees and departments.

## 9. Create Django Forms

Create the forms in `crudapp/forms.py`.

### DepartmentForm

Uses `forms.ModelForm` to generate the department form.

### EmployeeForm

Uses `forms.ModelForm` to generate the employee form with the required fields and widgets.

The employee form uses:

- `CheckboxSelectMultiple` for hobbies.
- `RadioSelect` for gender.
- `Select` for the department dropdown.
- `NumberInput` for age.
- `ClearableFileInput` for the profile photo.

Custom validation methods check that age is between 18 and 100 and that the photo size does not exceed 5 MB.

**Why?** Django forms simplify data entry, validation, and saving model records.

## 10. Create CRUD Views

Open `crudapp/views.py` and create views for departments and employees.

The views handle:

- **Create:** Add new records.
- **Read:** Display existing records.
- **Update:** Edit existing records.
- **Delete:** Remove records when permitted.

The employee creation view also attempts to send an email notification after saving a new employee.

**Why?** Views handle application logic and connect forms, models, and templates.

## 11. Configure Application URLs

Create or update `crudapp/urls.py` to define routes for employee and department operations.

Examples of routes include:

- `/employees/`
- `/employees/add/`
- `/employees/<id>/edit/`
- `/employees/<id>/delete/`
- `/departments/`
- `/departments/add/`
- `/departments/<id>/edit/`
- `/departments/<id>/delete/`

Include `crudapp.urls` in the main `crudproject/urls.py` file.

**Why?** URL patterns connect browser requests to the appropriate views.

## 12. Create HTML Templates

Create the HTML templates for:

- Employee list
- Employee creation
- Employee editing
- Employee deletion
- Department list
- Department creation
- Department editing
- Department deletion

Use Bootstrap classes to style the forms, tables, buttons, and navigation.

**Why?** Templates provide the user interface for performing CRUD operations.

## 13. Configure Profile Photo Uploads

Add the following settings to `crudproject/settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Configure media URL serving in the main URL configuration for development.

Ensure employee forms use `multipart/form-data` and the views pass uploaded files through `request.FILES`.

**Why?** These settings allow uploaded employee photos to be stored and displayed.

## 14. Configure Mailtrap Email

Create a `.env` file in the project root and add your Mailtrap SMTP credentials.

```dotenv
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_HOST_USER=your_mailtrap_username
EMAIL_HOST_PASSWORD=your_mailtrap_password
EMAIL_PORT=2525
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=django-app@example.com
```

Load these environment variables in `crudproject/settings.py` and configure Django's SMTP email backend.

**Why?** Mailtrap lets us test employee creation email notifications in a sandbox environment.

Keep your actual credentials private and do not commit `.env` to the repository.

## 15. Create and Apply Database Migrations

Create migration files:

```powershell
python manage.py makemigrations crudapp
```

**Why?** This generates migration files based on changes to the models.

Apply the migrations:

```powershell
python manage.py migrate
```

**Why?** This creates the required tables in the configured PostgreSQL database and applies Django's built-in migrations.

Check the application migration status:

```powershell
python manage.py showmigrations crudapp
```

## 16. Create a Superuser

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

**Why?** A superuser can access Django's administration site when the relevant models and admin configuration are registered.

## 17. Run the Application

Start the Django development server:

```powershell
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## 18. Test the Application

Test the following operations:

- Create, view, update, and delete departments.
- Create, view, update, and delete employees.
- Select a department from the dropdown.
- Select multiple hobbies using checkboxes.
- Choose gender using radio buttons.
- Upload an employee profile photo.
- Verify age and photo size validation.
- Verify that employee creation email notifications appear in Mailtrap.

## Conclusion

The application demonstrates Django CRUD operations with PostgreSQL, model relationships, ModelForms, field validation, image uploads, Bootstrap templates, and email notifications using Mailtrap.
