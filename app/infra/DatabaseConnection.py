
import psycopg2 as database

class DatabaseConnection:

    @staticmethod
    def get_connection():
        connection =  database.connect(
            host="localhost",
            port=5432,
            database="soundfire",
            user="postgres",
            password="1234"
        )
        connection.autocommit = True
        return connection