from flask import Flask, request, render_template

app = Flask(__name__)

# Home page route (GET method)
@app.route('/', methods=['GET'])
def home():
    return '''
        <form method="POST" action="/submit">
            <input type="text" name="username" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

# Route to handle form submission (POST method)
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')  # Get the value from the form
    return f'Hello, {username}! Thank you for submitting your name.'

if __name__ == '__main__':
    app.run(debug=True)
