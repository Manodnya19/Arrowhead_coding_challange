import sqlite3
import json
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            website TEXT,
            address_id INTEGER,
            company_id INTEGER,
            FOREIGN KEY (address_id) REFERENCES Addresses(id),
            FOREIGN KEY (company_id) REFERENCES Companies(id)
        )
    """)
    
    # Create Addresses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Addresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            street TEXT,
            suite TEXT,
            city TEXT,
            zipcode TEXT,
            latitude REAL,
            longitude REAL
        )
    """)
    
    # Create Companies table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            catchPhrase TEXT,
            bs TEXT
        )
    """)
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("SQLite database and tables created successfully.")


def insert_user_data(response_obj):
    # Parse the JSON data from the Response object
    if hasattr(response_obj, 'data'):  # Check if it's a Flask Response object
        json_data = json.loads(response_obj.data)
    else:
        json_data = response_obj  # Assume it's already parsed JSON

    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    for user in json_data:
        # Insert address and retrieve its ID
        cursor.execute("""
            INSERT INTO Addresses (street, suite, city, zipcode, latitude, longitude)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user['address']['street'],
            user['address']['suite'],
            user['address']['city'],
            user['address']['zipcode'],
            float(user['address']['geo']['lat']),
            float(user['address']['geo']['lng'])
        ))
        address_id = cursor.lastrowid

        # Insert company and retrieve its ID
        cursor.execute("""
            INSERT INTO Companies (name, catchPhrase, bs)
            VALUES (?, ?, ?)
        """, (
            user['company']['name'],
            user['company']['catchPhrase'],
            user['company']['bs']
        ))
        company_id = cursor.lastrowid

        # Insert user record
        cursor.execute("""
            INSERT INTO Users (id, name, username, email, phone, website, address_id, company_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user['id'],
            user['name'],
            user['username'],
            user['email'],
            user['phone'],
            user['website'],
            address_id,
            company_id
        ))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print("All records have been successfully inserted.")
