# bad_code.py

def connect_to_db():
    # DANGER 1: Hardcoded credentials
    password = "super_secret_password_123"
    print("Connecting with password: " + password)
    
    # DANGER 2: No error handling for file operations
    # If this file doesn't exist, the whole program will crash
    connection = open("database.txt", "r")
    return connection

def get_user_data(user_id):
    # DANGER 3: Insecure file access (Path Traversal vulnerability)
    # A user could pass something like "../../etc/passwd" as an ID
    path = "data/" + user_id + ".txt"
    with open(path, "r") as f:
        return f.read()