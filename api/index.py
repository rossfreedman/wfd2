from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# Keep only this basic route for now to test deployment 