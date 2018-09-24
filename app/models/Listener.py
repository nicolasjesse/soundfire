from app.models.Profile import Profile


class Listener(Profile):
    def __init__(self, code, name, email, password, picture):
        Profile.__init__(self, code, name, email, password, picture)
        self.__playlists = []
        self.__followers = []
        self.__following = []
        self.__liked_playlists = []

    def add_playlist(self, playlist_code):
        self.__playlists.append(playlist_code)

    def remove_playlist(self, playlist_code):
        self.__playlists.remove(playlist_code)

    def add_follower(self, user_code):
        self.__followers.append(user_code)

    def remove_follower(self, user_code):
        self.__followers.remove(user_code)

    def add_following(self, user_code):
        self.__following.append(user_code)

    def remove_following(self, user_code):
        self.__following.remove(user_code)

    def add_liked_playlist(self, playlist_code):
        self.__liked_playlists.append(playlist_code)

    def remove_liked_playlist(self, playlist_code):
        self.__liked_playlists.remove(playlist_code)

    @property
    def playlists(self):
        return self.__playlists

    @property
    def followers(self):
        return self.__followers

    @property
    def following(self):
        return self.__following

    @property
    def liked_playlists(self):
        return self.__liked_playlists
