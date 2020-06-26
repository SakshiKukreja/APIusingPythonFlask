from flask import Flask
app = Flask(__name__)


#how to call: https://<ip>/<username>
@app.route('/<username>/', methods = ['GET'])
def helloUser(username):
    return "Hey " + username + ", I am an API."

if __name__ == "__main__" :
    app.run()    