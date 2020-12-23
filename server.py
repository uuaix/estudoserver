import os
from flask import Flask, session, jsonify, url_for, request
from markupsafe import escape

app = Flask(__name__)

# # Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#

# Baisc Data Model 4 User ----------------

class User():
    def __construct__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image


users = []


def get_current_user():
    return session['loggeduser']


def get_all_users():
    return users


def set_user():
    newuser = User('Rodrigo', 'Light', './data/rod_profile.png')
    users.append(newuser)
    session['loggeduser'] = newuser


# ----------------------------------------


@app.route('/')
def index():
    if 'loggeduser' in session:
        return 'Logged in as %s' % escape(session['loggeduser'].username)
    return 'You are not logged in'


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['loggeduser'].username = request.form['username']
        return True


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('loggeduser', None)
    return True


@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }


@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])


# Functionality of the APP eSTudo ---------------------------------------------


@app.route("/get_classes")
def get_classes():
    classesList = []
    with os.scandir('./data/') as entries:
        for entry in entries:
            classesList.append(entry.name)
            print(entry.name)
            print(entry)
        return jsonify(classesList)


@app.route("/get_classes/<id>")
def get_class(id=None):
    media_url_list = []
    with os.scandir('./data/' + id) as entries:
        for entry in entries:
            print(entry.name)
            url = url_for('static', filename=entry.name)
            media_url_list.append(url)
    return jsonify(media_url_list)
