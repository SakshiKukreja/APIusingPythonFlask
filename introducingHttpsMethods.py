from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    return "Hey, This is specifying https methods for you"

@app.route('/onlyGet', methods = ['GET'])
def onlyGet():
    return "This request can only be done using \"GET\" method."

@app.route('/onlyPost', methods = ['POST'])
def onlyPost():
    return "This request can only be done using \"POST\" method."

if __name__ == "__main__":
    app.run()