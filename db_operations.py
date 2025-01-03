import sqlite3

class DatabaseManager:
    def __init__(self, db_path="db/face_recognition.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def fetch_users(self):
        query = """
            SELECT Users.user_id, Users.name,Users.photo_path, Departements.dep_name, Users.role
            FROM Users
            INNER JOIN Departements ON Users.dep_id = Departements.dep_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_users_from_db(self):
        # Query to fetch both department ID and name
        query = "SELECT user_id, name FROM Users"  # Adjust column names as per your database schema
        self.cursor.execute(query)
        return self.cursor.fetchall()  # Return the list of tuples (dep_id, dep_name)


    def add_user(self,name, photo_path, dep_id, role):
        """Create a new user."""
        query = "INSERT INTO Users (name, photo_path, dep_id, role) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (name, photo_path, dep_id, role))
        self.connection.commit()

    def update_user(self, user_id, name=None, photo_path=None, dep_id=None, role=None):
        """Update an existing user."""
        updates = []
        params = []
        if name:
            updates.append("name = ?")
            params.append(name)
        if photo_path:
            updates.append("photo_path = ?")
            params.append(photo_path)
        if dep_id:
            updates.append("dep_id = ?")
            params.append(dep_id)
        if role:
            updates.append("role = ?")
            params.append(role)

        params.append(user_id)
        query = f"UPDATE Users SET {', '.join(updates)} WHERE user_id = ?"
        self.cursor.execute(query, params)
        self.connection.commit()

    def delete_users(self, user_ids):
        query = "DELETE FROM Users WHERE user_id IN ({})".format(",".join(["?"] * len(user_ids)))
        self.cursor.execute(query, user_ids)
        self.connection.commit()

    def fetch_admins(self):
        query = """
            SELECT Admins.admin_id, Users.name, Admins.email, Admins.password
            FROM Admins
            INNER JOIN Users ON Admins.user_id = Users.user_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def add_admin(self, user_id, email, password):
        """Create a new admin."""
        query = "INSERT INTO Admins (user_id, email, password) VALUES (?, ?, ?)"
        self.cursor.execute(query, (user_id, email, password))
        self.connection.commit()
    
    def delete_admins(self, admin_ids):
        query = "DELETE FROM Admins WHERE admin_id IN ({})".format(",".join(["?"] * len(admin_ids)))
        self.cursor.execute(query, (admin_ids))
        self.connection.commit()

    def update_admin(self, admin_id,user=None ,email=None, password=None):
        """Update admin details."""
        updates = []
        values = []

        if user:
            updates.append("user_id = ?")
            values.append(user)
        
        if email:
            updates.append("email = ?")
            values.append(email)
        
        if password:
            updates.append("password = ?")
            values.append(password)

        if updates:  # Only proceed if there's something to update
            query = f"UPDATE Admins SET {', '.join(updates)} WHERE admin_id = ?"
            values.append(admin_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()


    def fetch_logs(self):
        """Read all logs and display user names instead of user IDs."""
        query = """
            SELECT 
                AccessLogs.log_id, 
                Users.name AS user_name, 
                AccessLogs.timestamp ,
                AccessLogs.emotion 
            FROM 
                AccessLogs
            INNER JOIN 
                Users ON AccessLogs.user_id = Users.user_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def fetch_departments(self):
        """Read all departments."""
        query = "SELECT * FROM Departements"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_departments_from_db(self):
        # Query to fetch both department ID and name
        query = "SELECT dep_id, dep_name FROM Departements"  # Adjust column names as per your database schema
        self.cursor.execute(query)
        return self.cursor.fetchall()  # Return the list of tuples (dep_id, dep_name)

    def add_department(self, dep_name):
        """Create a new department."""
        query = "INSERT INTO Departements (dep_name) VALUES (?)"
        self.cursor.execute(query, (dep_name,))
        self.connection.commit()

    def update_department(self, dep_id, dep_name):
        """Update a department."""
        query = "UPDATE Departements SET dep_name = ? WHERE dep_id = ?"
        self.cursor.execute(query, (dep_name, dep_id))
        self.connection.commit()

    def delete_department(self, dep_ids):
        """Delete a department."""
        query = "DELETE FROM Departements WHERE dep_id IN ({})".format(",".join(["?"] * len(dep_ids)))
        self.cursor.execute(query, (dep_ids))
        self.connection.commit()

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()
