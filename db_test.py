import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees"
    )
    
    if connection.is_connected():
        print("Connected to MySQL Server!")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM table1;")
        for row in cursor.fetchall():
            print(row)
            
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
