from app.infra import DatabaseConnection as db


class GenreRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_genre(self, genre):
        insert_sql = "INSERT INTO genre (description) VALUES ('%s')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % genre.description)
            return True
        except Exception:
            return False

    def update_genre(self, genre):
        update_sql = "UPDATE genre SET description = %s WHERE code = %d"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(update_sql % (genre.description, genre.code))
            return True
        except Exception:
            return False

    def del_genre(self, genre_code):
        del_sql = "DELETE FROM genre WHERE code = %s"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % genre_code)
            return True
        except Exception:
            return False

    def get_genres(self):
        get_sql = "SELECT code, description FROM genre"
        genre_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                genre_list.append(Genre(result[0], result[1]))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return genre_list

    def get_genre(self, genre_code):
        get_sql = "SELECT code, description FROM genre WHERE code = %s"
        genre = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % genre_code))
            result = cursor.fetchone()
            genre = Genre(result[0], result[1])
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return genre
