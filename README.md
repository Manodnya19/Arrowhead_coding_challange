# Features

1. Fetch User Data:
    Data is fetched from the API: https://jsonplaceholder.typicode.com/users.
    Fetched data is displayed in JSON format for better readability.

2. SQLite Database:
    A lightweight, serverless database is used.
    Database includes three tables: Users, Addresses, and Companies.

3. Raw SQL Queries:
    Sorting user records by name.
    Updating user email
    Filtering users based on geographic coordinates.

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

**main.py**

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

# Usage

Running the Program

1. Clone the repository.
2. Run main.py
```python
python main.py
```

# Why SQLite?
SQLite was chosen because it is lightweight, serverless, and ideal for local development. It allows us to demonstrate database operations without requiring additional setup.