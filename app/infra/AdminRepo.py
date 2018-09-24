from app.infra import DatabaseConnection as db
from app.models.Admin import Admin


class AdminRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_admin(self, admin):
        insert_sql = "INSERT INTO profile (name, email, password, picture, type) VALUES ('%s', '%s', '%s', '%s', '%s')"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(insert_sql, (admin.name, admin.email, admin.password, admin.picture, 'ADMIN'))
            return True
        except Exception:
            return False
    
    def update_admin(self, admin):
        update_sql = "UPDATE profile SET name = '%s', email = '%s', password = '%s', picture = '%s' WHERE code = '%d' AND type = 'ADMIN'"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(update_sql % (admin.name, admin.email, admin.password, admin.picture, admin.code))
            return True
        except Exception:
            return False

    def del_admin(self, admin_code):
        del_sql = "DELETE FROM profile WHERE code = ? AND  type = ?"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(del_sql, (admin_code, 'ADMIN'))
            return True
        except Exception:
            return False
    
    def get_admins(self):
        get_sql = "SELECT code, name, email, password, picture FROM profile WHERE type = 'ADMIN'"
        admin_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                admin_list.append(Admin(result[0], result[1], result[2], result[3], result[4]))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return admin_list

    def get_admin(self, admin_email):
        get_sql = "SELECT code, name, email, password, picture FROM profile WHERE email = '%s' AND type = 'ADMIN'"
        admin = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql %(admin_email))
            result = cursor.fetchone()
            admin = Admin(result[0], result[1], result[2], result[3], result[4])
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return admin
