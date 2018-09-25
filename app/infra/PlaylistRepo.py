from app.infra import DatabaseConnection as db
from app.models.Playlist import Playlist
from app.models.Profile import Profile


class PlaylistRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_playlist(self, playlist):
        insert_sql = "INSERT INTO playlist (name, publisher) VALUES ('%s', '%s')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % (playlist.name, playlist.publisher.code))
            return True
        except Exception:
            return False

    def update_playlist(self, playlist):
        update_sql = "UPDATE playlist SET name = '%s', publisher = '%d' WHERE code = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(update_sql, (playlist.name, playlist.publisher.code, playlist.code))
            return True
        except Exception:
            return False

    def del_playlist(self, playlist_code):
        del_sql = "DELETE FROM playlist WHERE code = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % playlist_code)
            return True
        except Exception:
            return False

    def get_playlists(self):
        get_sql = "SELECT pl.code, pl.name, pr.code, pr.name, pr.email, pr.picture FROM playlist pl JOIN profile pr ON pl.publisher = pr.code"
        playlists_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                playlists_list.append(Playlist(result[0], result[1], Profile(result[2], result[3], result[4], None, result[5])))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return playlists_list

    def get_playlist(self, playlist_code):
        get_sql = "SELECT pl.code, pl.name, pr.code, pr.name, pr.email, pr.picture FROM playlist pl JOIN profile pr ON pl.publisher = pr.code WHERE pl.code = '%d'"
        playlist = None 
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % playlist_code)
            result = cursor.fetchone()
            playlist = Playlist(result[0], result[1], Profile(result[2], result[3], result[4], None, result[5]))
        except Exception as error:
            raise("Error {0}".format(error))
        finally:
            return playlist
