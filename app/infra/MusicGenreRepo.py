from app.infra import DatabaseConnection as db
from app.models.Genre import Genre


class MusicGenreRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_music_genre(self, music_code, genre_code):
        insert_sql = "INSERT INTO music_genre (music, genre) VALUES ('%d', '%d')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % (int(music_code), int(genre_code)))
            return True
        except Exception:
            return False
    
    def del_music_genre(self, music_code, genre_code):
        del_sql = "DELETE FROM music_genre WHERE music = '%d' AND genre = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql %(music_code, genre_code))
            return True
        except Exception:
            return False
    
    def get_playlist_genres(self, playlist_code):
        get_sql = """SELECT code, description FROM genre g JOIN music_gerne mg 
                    ON mg.genre = g.code JOIN playlist_music pm ON mg.music = pm.music 
                    WHERE pm.playlist = '%d'"""
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
