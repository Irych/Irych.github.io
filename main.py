from flask import Flask, request, json, render_template, redirect, jsonify
import requests


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/is_auth')
def is_auth():
    return render_template('is_auth.html')


@app.route('/is_auth', methods=['POST', 'GET'])
def getvalue():
    global token
    if request.method == 'POST':
        token = request.form['token']
        return redirect('/friends')
    else:
        return '''<form method="POST">
                Enter access_token: <input type="text" name="token"><br>
                <input type="submit" value="Submit"><br>
                </form>'''


@app.route('/friends', methods=['POST', 'GET'])
def friends():
    res_users = requests.get(f'https://api.vk.com/method/friends.get?&order=random&count=5&fields=id,first_name,last_name&access_token={token}&v=5.103')
    items = (res_users.json()['response']['items'])
    user = requests.get(f'https://api.vk.com/method/users.get?&fields=id,first_name,last_name&access_token={token}&v=5.103')
    userdata = (user.json()['response'])
    username = (user.json()['response'][0]['first_name'])
    return render_template('friends.html', items=items, username=username)



if __name__ == "__main__":
    app.run()
