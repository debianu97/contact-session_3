import psycopg2

print("Python is running this file")

import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="assignment_db",
        user="postgres",
        password="oluwaseun",
        port=5432
    )

    print("Database connected successfully!")

    connection.close()

except psycopg2.OperationalError as error:
    print("Connection failed:", error)