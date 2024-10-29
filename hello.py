from flask import Flask, request, render_template
from markupsafe import escape
import docker

app = Flask(__name__)
app.config['SECRET_KEY'] = str(hex(id(123123123123)))
client = docker.from_env() #L4 docker

@app.route('/', methods=['GET', 'POST']) #helps put the https route of the function beneath
def base_page(): #return the template
    if request.method == 'POST': #L3 create form in index.html and also here
        docker_image = request.form['docker_image']
        command = request.form['command']
        client.containers.run("ubuntu", "echo hello world") #L4 docker
        return render_template('index.html')
    return render_template('index.html') #Lesson 2 => create template folder and an index.html file

#@app.route('/user/<username>') #helps put the https route of the function beneath
#def profile(username):
#    return f'{username}\'s profile'
#
#@app.route('/login', methods = ['GET','POST']) #helps put the https route of the function beneath
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True) # Start the server only if this script is run directly

