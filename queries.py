import sqlite3
import json

# Define SQL queries as static variables
SELECT_USER_COLUMNS = """
    SELECT 
        u.id,
        u.name,
        u.username,
        u.email,
        u.phone,
        u.website,
        a.street,
        a.suite,
        a.city,
        a.zipcode,
        a.latitude,
        a.longitude,
        c.name AS company_name,
        c.catchPhrase AS company_catchPhrase,
        c.bs AS company_bs
    FROM 
        Users u
    JOIN 
        Addresses a ON u.address_id = a.id
    JOIN 
        Companies c ON u.company_id = c.id
"""

def connect_to_db():
    """Helper function to connect to the SQLite database."""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None, None

def close_db_connection(conn):
    """Helper function to close the SQLite database connection."""
    conn.close()

def format_user_data(record):
    """Helper function to format the record into the desired JSON structure."""
    columns = [
        "id", "name", "username", "email", "phone", "website", 
        "street", "suite", "city", "zipcode", "latitude", "longitude",
        "company_name", "company_catchPhrase", "company_bs"
    ]
    user_data = dict(zip(columns, record))
    
    # Format the address and company details as nested objects
    user_data["address"] = {
        "street": user_data.pop("street"),
        "suite": user_data.pop("suite"),
        "city": user_data.pop("city"),
        "zipcode": user_data.pop("zipcode"),
        "geo": {
            "lat": user_data.pop("latitude"),
            "lng": user_data.pop("longitude")
        }
    }
    user_data["company"] = {
        "name": user_data.pop("company_name"),
        "catchPhrase": user_data.pop("company_catchPhrase"),
        "bs": user_data.pop("company_bs")
    }

    return user_data

def sort_records_by_name():
    conn, cursor = connect_to_db()

    # Execute the SQL query to sort records by name
    cursor.execute(SELECT_USER_COLUMNS + " ORDER BY u.name ASC;")
    
    # Fetch all sorted records
    sorted_records = cursor.fetchall()

    # Format and print the sorted records in JSON format
    for record in sorted_records:
        user_data = format_user_data(record)
        print(json.dumps(user_data, indent=4))

    # Close the connection
    close_db_connection(conn)

def update_email(user_id, new_email):
    try:
        conn, cursor = connect_to_db()
        
        # Enable foreign keys
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Update the email address for the specified user ID
        cursor.execute("""
            UPDATE Users
            SET email = ?
            WHERE id = ?
        """, (new_email, user_id))
        
        # Commit changes
        conn.commit()
        
        # Check if the update was successful
        if cursor.rowcount > 0:
            print(f"User with ID {user_id} had their email updated to {new_email}.")
        else:
            print(f"No user found with ID {user_id}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        close_db_connection(conn)

def filter_users_by_longitude(min_longitude):
    try:
        conn, cursor = connect_to_db()
        
        # SQL query to filter users by longitude
        cursor.execute(SELECT_USER_COLUMNS + " WHERE a.longitude > ?;", (min_longitude,))
        results = cursor.fetchall()
        
        # Prepare data in JSON format
        users_list = [format_user_data(row) for row in results]

        # If there are results, print in JSON format
        if users_list:
            print(json.dumps(users_list, indent=4))
        else:
            print(f"No users found with longitude greater than {min_longitude}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        close_db_connection(conn)
