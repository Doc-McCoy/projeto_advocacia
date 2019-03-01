from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, current_user, login_user, \
    logout_user, login_required, UserMixin

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = 'wtfisthis'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
    return "Entrou na area protegida!"

@app.route('/login')
def login():
    login_user(User(1))
    return "You are logged in"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "Foi embora"

if __name__ == '__main__':
    app.run(debug=True)