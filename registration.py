import sqlite3

def search_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE student_id = '" + student_id + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()

    return result

def login(username, password):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    return result 
