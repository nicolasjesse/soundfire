from flask import request, session, render_template, redirect
from app import app 
from app.infra.AdminRepo import AdminRepo
from app.infra.ListenerRepo import ListenerRepo
from app.infra.FollowersRepo import FollowersRepo
from app.models.Admin import Admin
from app.models.Listener import Listener
import base64
import ast


admin_repo = AdminRepo()
listener_repo = ListenerRepo()
followers_repo = FollowersRepo()


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
    return "Inexistente"


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


@app.route("/upload-music", methods=["GET", "POST"])
def upload_teste():
    if request.method == "GET":
        return render_template("upload-music.html")
    fmusic = request.files["music"]
    music = base64.b64encode(fmusic.read()).decode('utf-8').replace('\n', '')
    return "<html style='background-color: black; text-align: center'><body><h1 style='background-color: gray'>Playli" \
           "st Aleatoria </h1><audio style='width:80%' controls src='data:audio/mp3;base64," + music + "'/></body></h" \
                                                                                                       "tml>"


@app.errorhandler(404)
def page_not_found(error):
    return render_template("to_index.html", login=False)