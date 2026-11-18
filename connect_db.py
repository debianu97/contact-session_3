import psycopg2 


connection = psycopg2.connect(
    host="localhost",
    database="assignment_db",
    user="postgres",
    password="oluwaseun",
    port=5432
)

# print("Database connected successfully")



cursor = connection.cursor()

name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
department = input("Enter student's department: ")

cursor.execute("""
    INSERT INTO students (name, age, department)
    VALUES(%s, %s, %s)
""", (name, age, department))

connection.commit()
print("Student added successfully")

cursor.execute("SELECT * FROM students ORDER BY id ASC")

students_list = cursor.fetchall()

for student in students_list:
    print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")


# cursor.execute("""
#     UPDATE students
#     SET department = %s
#     where id = %s
# """, ("Software Engineering", 1))

# connection.commit()
# print("Student updated successfully")
# cursor.execute("SELECT * FROM students")
# first_student = cursor.fetchone()
# print(first_student)

   
