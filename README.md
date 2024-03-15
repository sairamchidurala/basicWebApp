# Basic Web Application

This is a simple web application built with Django that allows users to input data, validate it, store it in a database, retrieve it, and display it in a table format.

## Setup and Installation

1. Clone the repository to your local machine:

`git clone https://github.com/sairamchidurala/basicWebApp.git`


2. Navigate to the project directory:

`cd basicWebApp`


3. Create a virtual envirnoment and activate it.

# To create a virtual environment and activate it, follow these steps:
## **For Windows:**

1. **Create Virtual Environment:**
   Launch Command Prompt and navigate to the directory where you wish to establish the virtual environment.
   Execute the following command to form a virtual environment named "venv":

   `python3 -m venv venv`

3. **Activate Virtual Environment:**
   Move to the directory containing the virtual environment and initiate the activation script:

   `venv\Scripts\activate`

   Upon activation, you'll notice "(venv)" displayed at the beginning of the command prompt, indicating the active virtual environment.

## **For macOS:**

1. **Create Virtual Environment:**
   Open the Terminal and navigate to the desired directory for the virtual environment.
   Utilize the following command to generate a virtual environment named "venv":

   `python3 -m venv venv`

3. **Activate Virtual Environment:**
   Navigate to the directory holding the virtual environment and run the activation script:

   `source venv/bin/activate`
   
   Upon activation, you can proceed to install dependencies and execute Python scripts without impacting the system-wide Python installation. To deactivate the virtual environment, simply execute the `deactivate` command in the Command Prompt or Terminal.


5. Install dependencies using pip:

`pip install -r requirements.txt`


6. Apply migrations to set up the database schema:

`python3 manage.py migrate`


7. Running the Application

`python3 manage.py runserver`


Access the application in your web browser at http://127.0.0.1:8000/.

## Features
User Input Form: Allows users to input their name, email, age, and date of birth.

Form Validation: Ensures data validity through client-side and server-side validation.

Data Storage: Stores valid user data in an SQLite database.

Data Retrieval: Displays stored data in a tabular format on the data table page.

User-friendly Interface: Utilizes Bootstrap for styling, creating a clean and user-friendly interface.
