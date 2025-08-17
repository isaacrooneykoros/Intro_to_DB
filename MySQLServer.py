import mysql.connector

try:
    # Connect to MySQL (without selecting a DB yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="isaac5480"   # change to your root password
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        cursor = connection.cursor()

        # ✅ Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database alx_book_store ensured.")

        # Switch to the database
        cursor.execute("USE alx_book_store;")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
