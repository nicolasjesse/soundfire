class Playlist:
    def __init__(self, code, name, genre, publisher):
        self.__code = code
        self.__name = name
        self.__genre = genre
        self.__publisher = publisher
        self.__musics = []

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def genre(self):
        return self.__genre

    @property
    def publisher(self):
        return self.__publisher

    @property
    def musics(self):
        return self.__musics

    @code.setter
    def code(self, new_code):
        self.__code = new_code

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    @publisher.setter
    def publisher(self, new_publisher):
        self.__publisher = new_publisher

    def add_music(self, music):
        self.__musics.append(music)

    def remove_music(self, music_code):
        self.musics.remove(music_code)
