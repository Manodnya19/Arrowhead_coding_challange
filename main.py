from fetch import fetch_user_data, display_records
from insert import create_database, insert_user_data
from queries import sort_records_by_name, update_email, filter_users_by_longitude

def main():
    print("=" * 60)
    print("USER DATA PROCESSING SYSTEM")
    print("=" * 60)

    # Step 1: Fetch user data from API
    print("\nFetching user data from API...")
    user_data = fetch_user_data()

    if user_data:
        print("\nDisplaying fetched user data:")
        display_records(user_data)

        # Step 2: Create database and insert data
        print("\nCreating SQLite database and inserting data...")
        create_database()
        insert_user_data(user_data)

        # Step 3: Queries
        print("\nSorting user records by name...")
        print("-" * 40)
        sort_records_by_name()

        print("\nUpdating email for user with ID 9...")
        print("-" * 40)
        update_email(9, "coding@arrowheadcu.org")

        print("\nFiltering users by longitude > -110.455...")
        print("-" * 40)
        filter_users_by_longitude(-110.455)
    else:
        print("No data retrieved from API. Exiting.")

if __name__ == "__main__":
    main()
