from app.infra import DatabaseConnection as db


class PlaylistLikesRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def like(self, playlist_code, profile_code):
        insert_sql = "INSERT INTO liked_playlists (playlist, profile) VALUES ('%d', '%d')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % (playlist_code, profile_code))
            return True
        except Exception:
            return False

    def unlike(self, playlist_code, profile_code):
        del_sql = "DELETE FROM liked_playlists WHERE playlist = '%d' AND profile_code = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(del_sql % (playlist_code, profile_code))
            return True
        except Exception:
            return False

    def count_likes(self, playlist_code):
        count_sql = "SELECT count(*) FROM liked_playlists WHERE playlist_code = '%d'"
        count_likes = 0
        try:
            cursor = self.__connection.cursor()
            cursor.execute(count_sql % playlist_code)
            count_likes = cursor.fetchone()
        except (Exception) as error:
            raise ("Error: {0}".format(error))
        return count_likes
