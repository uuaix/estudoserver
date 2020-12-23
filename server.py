import os
from flask import Flask
app = Flask(__name__)

class User():
	__construct__(self, username, theme, image):
		self.username = username
		self.theme = theme
		self.image = image

user = User('Rodrigo', 'Light', './media/rod_profile.png')

@app.route('/')
def hello_world():
    return 'Hello, World!'

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

medialist = None

with os.scandir('media/') as entries:
		medialist = entries
    for entry in entries:
        print(entry.name)
        url_for('static', filename='entry.name')

@app.route("/medialist")
def get_medialist():
    return medialist
