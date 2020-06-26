from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "It's for home page"
    
@app.route('/hello/')
def hello():
    return "Hey, Welcome to your first application"

if __name__ == "__main__":
    app.run()