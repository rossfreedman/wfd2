from flask import Flask, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Print current directory and list files for debugging
        current_dir = os.getcwd()
        files = os.listdir(current_dir)
        
        # Try to list the data directory
        data_dir = os.path.join(current_dir, 'data')
        if os.path.exists(data_dir):
            data_files = os.listdir(data_dir)
        else:
            data_files = "Data directory not found"
        
        return f"""
        Current directory: {current_dir}
        Files in current directory: {files}
        Data directory files: {data_files}
        """
    except Exception as e:
        return f"Debug Error: {str(e)}", 500

# Add any other routes you had here