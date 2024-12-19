# Features

1. Fetch User Data:
    Data is fetched from the API: https://jsonplaceholder.typicode.com/users.
    Fetched data is displayed in JSON format for better readability.

2. SQLite Database:
    A lightweight, serverless database is used.
    Database includes three tables: Users, Addresses, and Companies.

3. Raw SQL Queries:
    - Sorting user records by name.
    - Updating user email
    - Filtering users based on geographic coordinates.

4. Readable Output:
    Outputs are formatted in JSON and separated by clear visual markers

# Prerequisites

1. Install latest version of python  
Python 3.x: Ensure Python is installed on your system. You can download it from the official Python website.
2. Install requests
```python
pip install requests
```
3. SQLite: 
No separate installation is needed, as SQLite is included with Python by default.

# How It Works

**app.py**

This is the entry point of the application. It runs the functions which:
1. Fetches user data from the API.
2. Displays fetched data in a readable format.
3. Creates the database schema and populates it with fetched data.
4. Performs SQL queries to:

**fetch.py**

Responsible for:
1. Fetching user data from the API.
2. Displaying fetched data in JSON format for clarity.

**insert.py**

Handles database operations:
1. Creates tables (Users, Addresses, Companies) with relationships.
2. Inserts fetched user data into the database.

**queries.py**

Contains functions to perform SQL operations:
1. Sortes the user data by Name
2. Updates the email address for a specific user by ID.
3. Filters and displays users with longitude greater than a given value.

### How the UI Works
1. Fetch Data: Click the "Fetch Data" button to retrieve user data from a remote API This data will be displayed in a structured format.
2. Create Database: Clicking the "Create database" button will create a database.
3. Insert Data: Clicking the "Insert Data" button will insert data into the database.
4. Sort Data: Clicking the "Sort Data" button will sort the user data by name and display the sorted list.
5. Update Email: This allows you to update a user's email (you can modify this functionality).
6. Filter Users: This allows you to filter users based on their longitude and display the filtered data.

# How to Run

Running the Program

1. Clone the repository.
```console
git clone https://github.com/Manodnya19/Arrowhead_coding_challange.git
cd Arrowhead_coding_challange
```
2. Install Flask and Requests: 
```python
pip install Flask requests
```
3. Run the app:
```python
python app.py
```
4. Access the application: Open your browser and visit the following URL to interact with the app:
```console
http://localhost:5000
```
5. (Optional)
If you get the error : 
"Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port."
- Update the port number in app.py. 
- Find port = 5000 in app.py and update it to any desired port number.

# Why SQLite?
SQLite was chosen because it is lightweight, serverless, and ideal for local development. It allows us to demonstrate database operations without requiring additional setup.