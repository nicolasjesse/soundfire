from app.infra import DatabaseConnection as db
from app.models.Music import Music
from app.models.Genre import Genre


class PlaylistMusicRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_playlist_music(self, playlist_code, music_code):
        insert_sql = "INSERT INTO playlist_music (playlist, music) VALUES ('%d', '%d')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % (playlist_code, music_code))
            return True
        except Exception:
            return False
    
    def del_playlist_music(self, playlist_code, music_code):
        del_sql = "DELETE FROM playlist_music WHERE playlist = '%d' AND music = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % (playlist_code, music_code))
            return True
        except Exception:
            return False
    
    def get_playlist_musics(self, playlist_code):
        get_sql = """SELECT m.code, m.name, m.artist, m.content, g.code, g.description FROM music m JOIN playlist_music pm 
                    ON pm.music = m.code JOIN music_genre mg ON m.code = mg.music JOIN genre g
                    ON g.code = mg.genre WHERE pm.playlist = '%d'"""
        music_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % playlist_code)
            results = cursor.fetchall()
            for result in results:
                music = Music(result[0], result[1], result[2], result[3])
                music.genre = Genre(result[4], result[5])
                music_list.append(music)
        except Exception as error:
            print(error)
            raise("Error: {0}".format(error))
        finally:
            return music_list
