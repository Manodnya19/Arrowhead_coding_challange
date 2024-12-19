import requests
import json
from flask import Flask, Response

def fetch_user_data():
    # URL to fetch user data from
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # user_data = response.json()
        return Response(response.content, content_type='application/json')
        # return user_data
    else:
        print("Failed to retrieve data")
        return None

def display_records(user_data):
    """
    Display all user records in a formatted manner.
    """
    if not user_data:
        print("No user data to display.")
        return
    
    # print("\nDisplaying all user records:\n")
    for user in user_data:
        print(json.dumps(user, indent=4))
        print("-" * 40)  # Separator for better readability

