from app.infra import DatabaseConnection as db


class MusicRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_music(self, music):
        insert_sql = "INSERT INTO music (name, artist, content) VALUES ('%s', '%s', '%s')"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(insert_sql % (music.name, music.artist, music.content))
            return True
        except Exception:
            return False
    
    def update_music(self, music):
        update_sql = "UPDATE music SET name = '%s', artist = '%s', content = '%s' WHERE code = '%d'"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(update_sql, (music.name, music.artist, music.content, music.code))
            return True
        except Exception:
            return False

    def del_music(self, music_code):
        del_sql = "DELETE FROM profile WHERE code = '%d'"
        try:
            cursor = self.__connection.cursor() 
            cursor.execute(del_sql % music_code)
            return True
        except Exception:
            return False
    
    def get_musics(self):
        get_sql = "SELECT code, name, artist, content FROM music"
        music_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                music_list.append(Music(result[0], result[1], result[2], result[3]))
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return music_list

    def get_music(self, music_code):
        get_sql = "SELECT code, name, artist, content FROM music WHERE code = '%d'"
        music = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % music_code)
            result = cursor.fetchone()
            music = Music(result[0], result[1], result[2], result[3])
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return music
