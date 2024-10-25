from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/') #helps put the https route of the function beneath
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/user/<username>') #helps put the https route of the function beneath
def profile(username):
    return f'{username}\'s profile'

@app.route('/login', methods = ['GET','POST']) #helps put the https route of the function beneath
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True) # Start the server only if this script is run directly

