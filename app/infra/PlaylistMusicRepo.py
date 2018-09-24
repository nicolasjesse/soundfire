from app.infra import DatabaseConnection as db


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
        get_sql = """SELECT code, name, artist, content FROM music m JOIN playlist_music pm 
                    ON pm.music = m.code WHERE pm.playlist = '%d'"""
        music_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % playlist_code)
            results = cursor.fetchall()
            for result in results:
                music_list.append( Music(result[0], result[1], result[2], result[3]))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return music_list
