from flask import Flask, jsonify, request, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

# ... rest of your code ...

# Change the last part to:
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

# Remove the if __name__ == '__main__' block 