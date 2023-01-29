from werkzeug.exceptions import HTTPException
from flask import Flask, request, Response, render_template, redirect, make_response
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import utils

ACCOUNTS = {
    "guest": "password1234",
    "admin": get_random_bytes(32).hex()
}

KEY = get_random_bytes(AES.block_size)
FLAG = "UWA{cH1aM0_1_p1nGvIni!1}"

app = Flask(__name__, static_url_path='/', static_folder='static/')


@app.route('/penguin-dashboard', methods=['GET'])
def dashboard():
    auth_cookie = request.cookies.get('auth_cookie', None)
    if auth_cookie is None:
        return redirect('/login')
    
    try:
        username = utils.decrypt_auth_cookie(KEY, auth_cookie)
    except:
        resp: Response = make_response(redirect('/login'))
        resp.delete_cookie('auth_cookie')
        return resp

    if not username in ACCOUNTS:
        resp: Response = make_response(redirect('/login'))
        resp.delete_cookie('auth_cookie')
        return resp

    return render_template('dashboard.html', flag=FLAG, username=username)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username: str = request.form.get("username", None)
    if username is None:
        return render_template("login.html", error="Missing username")
    
    if not username in ACCOUNTS:
        return render_template("login.html", error="Invalid credentials")

    is_auth = ACCOUNTS[username] == request.form.get("password", "")

    if is_auth:
        resp: Response = make_response(redirect('/penguin-dashboard'))
        resp.set_cookie("auth_cookie", utils.encrypt_username(KEY, username.encode()), httponly=True)
        return resp

    return render_template("login.html", error="Invalid credentials")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
