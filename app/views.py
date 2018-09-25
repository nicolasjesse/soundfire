from flask import request, session, render_template, redirect
from app import app 
from app.infra.AdminRepo import AdminRepo
from app.infra.ListenerRepo import ListenerRepo
from app.infra.FollowersRepo import FollowersRepo
from app.infra.PlaylistRepo import PlaylistRepo
from app.infra.PlaylistMusicRepo import PlaylistMusicRepo
from app.infra.MusicRepo import MusicRepo
from app.infra.GenreRepo import GenreRepo
from app.infra.MusicGenreRepo import MusicGenreRepo
from app.infra.PlaylistMusicRepo import PlaylistMusicRepo
from app.models.Admin import Admin
from app.models.Profile import Profile
from app.models.Listener import Listener
from app.models.Playlist import Playlist
from app.models.Music import Music
from app.models.Genre import Genre
import base64
import ast


admin_repo = AdminRepo()
listener_repo = ListenerRepo()
followers_repo = FollowersRepo()
playlist_repo = PlaylistRepo()
playlist_music_repo = PlaylistMusicRepo()
genre_repo = GenreRepo()
music_repo = MusicRepo()
music_genre_repo = MusicGenreRepo()
playlist_music_repo = PlaylistMusicRepo()

@app.route("/")
def index():
    if session:
        return redirect("/home")
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    profile = request.form["profile"]
    if profile == "ADMIN":
        admin = admin_repo.get_admin(email)
        if admin is not None:
            if admin.password == password:
                session["user"] = email
                session["type"] = profile
                return redirect("/home")
        else:
            return render_template("to_index.html", login=True)
    elif profile == "LISTENER":
        listener = listener_repo.get_listener(email)
        if listener is not None:
            session["user"] = email
            session["type"] = profile
            return redirect("/home")
        else:
            return render_template("to_index.html", login=True)


@app.route("/home")
def home():
    if session["type"] == 'ADMIN':
        admin = admin_repo.get_admin(session["user"])
        return render_template("home.html", username=admin.name, picture=admin.picture)
    elif session["type"] == 'LISTENER':
        listener = listener_repo.get_listener(session["user"])
        return render_template("home.html", username=listener.name, picture=listener.picture)


@app.route("/user/<int:code>")
def show_user_profile(code):
    user = admin_repo.get_admin(session["user"])
    if user is None:
        user = listener_repo.get_listener(session["user"])
    session["user_visited"] = code
    followers = followers_repo.get_followers(session["user_visited"])
    listeners = listener_repo.get_listeners()
    admins = admin_repo.get_admins()
    for listener in listeners:
        if listener.code == code:
            return render_template("user.html", username=listener.name, picture=listener.picture,
                                   follow=(user.code in followers))
    for admin in admins:
        if admin.code == code:
            return render_template("user.html", username=admin.name, picture=admin.picture,
                                   follow=(user.code in followers))
    return "Usuário Inexistente!"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        picture = request.files['picture']
        if picture is not None:
            picture = base64.b64encode(picture.read()).decode('utf-8').replace('\n', '')
        listener = Listener(0, name, email, password, picture)
        sucess = listener_repo.add_listener(listener)
        print(sucess)
        return redirect("/")
    return render_template("signup.html", profile="LISTENER")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/follow", methods=["GET", "POST"])
def follow():
    admins = admin_repo.get_admins()
    listeners = listener_repo.get_listeners()
    for admin in admins:
        if session["user"] == admin.email:
            followers_repo.follow(admin.code, session["user_visited"])
            return redirect("/user/%d" % session["user_visited"])
    for listener in listeners:
        if session["user"] == listener.email:
            followers_repo.follow(listener.code, session["user_visited"])
            return redirect("/user/%d" % session["user_visited"])
    return False


@app.route("/unfollow")
def unfollow():
    user = admin_repo.get_admin(session["user"])
    if user is None:
        user = listener_repo.get_listener(session["user"])
    followers_repo.unfollow(user.code, session["user_visited"])
    return redirect("/user/%d" % session["user_visited"])


@app.route("/playlists", methods=["GET", "POST"])
def playlists():
    if request.method == "GET":
        playlists = playlist_repo.get_playlists()
        return render_template("playlists.html", playlists=playlists)

@app.route("/playlists/<int:code>")
def playlist(code):
    playlist = playlist_repo.get_playlist(code)
    playlist.musics = playlist_music_repo.get_playlist_musics(code)
    genres = genre_repo.get_genres()
    return render_template("playlist.html", playlist=playlist, genres=genres)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    if request.method == "POST":
        name = request.form["name"]
        publisher = listener_repo.get_listener(session["user"])
        if publisher is None:
            publisher = admin_repo.get_admin(session["user"])
        playlist_repo.add_playlist(Playlist(0, name, publisher))
        return redirect("/playlists")
    return render_template("add_playlist.html")


@app.route("/playlists/<int:code>/music/add", methods=["POST"])
def add_music_playlist(code):
    name = request.form["name"]
    artist = request.form["artist"]
    genre = request.form["genre"]
    music_file = request.files["music"]
    content = ""
    if music_file is not None:
        content = base64.b64encode(music_file.read()).decode('utf-8').replace('\n', '')
    music_repo.add_music(Music(0, name, artist, content))
    music = music_repo.get_music(name, artist)
    music_genre_repo.add_music_genre(music.code, genre)
    playlist_music_repo.add_playlist_music(code, music.code)
    return redirect("/playlists/%d" % code)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("to_index.html", login=False)