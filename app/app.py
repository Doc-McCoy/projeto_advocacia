from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

app             = Flask(__name__)
app.secret_key  = "wtfisthis"
login_manager   = LoginManager(app)

# ================================================
class User(UserMixin):
    def __init__(self, id):
        self.id = login

@login_manager.user_loader
def load_user(login):
    return User(login)

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash("aqui não, negão!")
    return redirect(url_for('login'))

# ================================================
def checkLoginValid(user, password):
    if user == 'admin' and password == 'root':
        return True
    else:
        return False

# ================================================
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    elif request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        if not (user and password):
            flash("Digita a porra do user e a senha né caralho!")
            return redirect(url_for('login'))
        
        if checkLoginValid(user, password):
            userToLoad = User(user)
            login_user(userToLoad)
            return redirect(url_for('home'))
        else:
            flash("Usuário ou senha incorreto")
            return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('login'))

# ================================================
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
