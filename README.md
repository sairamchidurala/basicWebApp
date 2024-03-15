# Basic Web Application

This is a simple web application built with Django that allows users to input data, validate it, store it in a database, retrieve it, and display it in a table format.

## Setup and Installation

1. Clone the repository to your local machine:
 ```git clone https://github.com/sairamchidurala/basicWebApp.git```

2. Navigate to the project directory:
```cd basicWebApp```

3. Install dependencies using pip:
```pip install -r requirements.txt```

4. Apply migrations to set up the database schema:
```python manage.py migrate```

5. Running the Application
```python manage.py runserver```

7. Start the Django development server:
```python manage.py runserver```

Access the application in your web browser at http://127.0.0.1:8000/.

## Features
User Input Form: Allows users to input their name, email, age, and date of birth.

Form Validation: Ensures data validity through client-side and server-side validation.

Data Storage: Stores valid user data in a SQLite database.

Data Retrieval: Displays stored data in a tabular format on the data table page.

User-friendly Interface: Utilizes Bootstrap for styling, creating a clean and user-friendly interface.
