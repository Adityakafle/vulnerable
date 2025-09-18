# vulnerable_test.py
import sqlite3

def get_user_info(user_id):
    # WARNING: intentionally vulnerable to SQL injection for testing
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
    cursor.execute("INSERT INTO users VALUES (2, 'Bob')")
    
    # Vulnerable query
    query = f"SELECT name FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    return None

if __name__ == "__main__":
    user_input = input("Enter user ID: ")
    print("User name:", get_user_info(user_input))
