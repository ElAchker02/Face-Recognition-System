import sqlite3


class DatabaseManager:
    def __init__(self, db_path="db/face_recognition.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def fetch_users(self):
        query = """
        SELECT user_id, name, photo_path, dep_name, role
        FROM Users
        LEFT JOIN Departements ON Users.dep_id = Departements.dep_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_admins(self):
        query = """
        SELECT admin_id, name, email, password
        FROM Admins
        LEFT JOIN Users ON Admins.user_id = Users.user_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_logs(self):
        query = """
        SELECT log_id, timestamp, emotion
        FROM AccessLogs
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_departments(self):
        query = """
        SELECT dep_id, dep_name
        FROM Departements
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
