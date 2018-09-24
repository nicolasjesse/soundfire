from app.infra import DatabaseConnection as db


class PlaylistGenreRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_playlist_genre(self, playlist_code, genre_code):
        insert_sql = "INSERT INTO playlist_genre (playlist, genre) VALUES ('%d', '%d')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql %(playlist_code, genre_code))
            return True
        except Exception:
            return False
    
    def del_playlist_genre(self, playlist_code, genre_code):
        del_sql = "DELETE FROM playlist_genre WHERE playlist = '%d' AND genre = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % (playlist_code, genre_code))
            return True
        except Exception:
            return False
    
    def get_playlist_genres(self, playlist_code):
        get_sql = """SELECT code, description FROM genre g JOIN playlist_genre pg 
                    ON pg.genre = g.code WHERE pg.playlist = '%d'"""
        genre_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % playlist_code)
            results = cursor.fetchall()
            for result in results:
                genre_list.append(Genre(result[0], result[1]))
        except (Exception) as error:
            raise("Error: {0}".format(error))
        finally:
            return genre_list
