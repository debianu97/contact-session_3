import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="assignment_db",
    user="postgres",
    password="oluwaseun",
    port=5432
)

cursor = connection.cursor()
print("Cursor created successfully!")

cursor.execute("INSERT INTO tasks (title) VALUES (%s)", ("Study Python",))

connection.commit()

cursor.execute("SELECT * FROM tasks")

tasks = cursor.fetchall()

print(tasks)