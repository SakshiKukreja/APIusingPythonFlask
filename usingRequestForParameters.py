from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def sayHello():
    username = ""
    if request.method == 'POST':
        username = request.form['username']         #for post params are sent in body, thus form is used.
    else:
        username = request.args['username']         #to get params from url, we use args
    return "Hello " + username

if __name__ == "__main__":
    app.run()