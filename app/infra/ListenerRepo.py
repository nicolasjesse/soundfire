from app.infra import DatabaseConnection as db
from app.models.Listener import Listener


class ListenerRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_listener(self, listener):
        insert_sql = "INSERT INTO profile (name, email, password, picture, type) VALUES ('%s', '%s', '%s', '%s', '%s')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql %(listener.name, listener.email, listener.password, listener.picture, 'LISTENER'))
            return True
        except Exception:
            return False

    def update_listener(self, listener):
        update_sql = "UPDATE profile SET name = '%s', email = '%s', password = '%s', picture = '%s' WHERE code = " \
                     "'%d' AND type = 'LISTENER'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(update_sql % (listener.name, listener.email, listener.password, listener.picture, listener.code))
            return True
        except (Exception):
            return False

    def del_listener(self, listener_code):
        del_sql = "DELETE FROM profile WHERE code = '%d' AND  type = '%s'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % (listener_code, 'LISTENER'))
            return True
        except Exception:
            return False

    def get_listeners(self):
        get_sql = "SELECT code, name, email, password, picture FROM profile WHERE type = 'LISTENER'"
        listener_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                listener_list.append(Listener(result[0], result[1], result[2], result[3], result[4]))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return listener_list

    def get_listener(self, listener_email):
        get_sql = "SELECT code, name, email, password, picture FROM profile WHERE email = '%s' AND type = 'LISTENER'"
        listener = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql %(listener_email))
            result = cursor.fetchone()
            listener = Listener(result[0], result[1], result[2], result[3], result[4])
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return listener
