import mysql.connector

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="isaac5480",   # change to your root password
        database="alx_book_store"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
