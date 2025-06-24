import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",      # Replace with your MySQL username
            password="your_password"   # Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Try to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")

    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
    else:
        # Close the connection if it was opened successfully
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()
