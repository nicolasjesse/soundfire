class Music:
    def __init__(self, code, name, artist, content):
        self.__code = code
        self.__name = name
        self.__artist = artist
        self.__content = content
        self.__genre = None

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def artist(self):
        return self.__artist

    @property
    def genre(self):
        return self.__genre

    @property
    def content(self):
        return self.__content

    @code.setter
    def code(self, new_code):
        self.__code = new_code

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @artist.setter
    def artist(self, new_artist):
        self.__artist = new_artist

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    @content.setter
    def content(self, new_content):
        self.__content = new_content
