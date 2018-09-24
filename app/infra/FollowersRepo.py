from app.infra import DatabaseConnection as db


class FollowersRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()
    
    def follow(self, follower, followed):
        insert_sql = "INSERT INTO followers (follower, followed) VALUES ('%d', '%d')"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(insert_sql % (follower, followed))
            return True
        except Exception:
            return False
    
    def unfollow(self, follower, followed):
        del_sql = "DELETE FROM followers WHERE follower = '%d' AND followed = '%d'"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(del_sql % (follower, followed))
            return True
        except Exception:
            return False

    def count_followers(self, followed):
        count_sql = "SELECT count(*) FROM followers WHERE followed = '%d'"
        count_followers = 0
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(count_sql % followed)
            count_followers = cursor.fetchall()
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return count_followers

    def count_followed(self, follower):
        count_sql = "SELECT count(*) FROM followers WHERE follower = '%d'"
        count_followeds = 0
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(count_sql % follower)
            count_followeds = cursor.fetchone()
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return count_followeds

    def get_followers(self, followed):
        get_sql = "SELECT follower FROM followers WHERE followed = '%s'"
        followers_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % followed)
            results = cursor.fetchall()
            for result in results:
                followers_list.append(result[0])
        except Exception as error:
            print("Error: {0}".format(error))
        finally:
            return followers_list