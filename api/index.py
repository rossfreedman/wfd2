from flask import Flask, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Get the absolute path to the CSV file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'data', 'RestaurantData.csv')
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Get a random restaurant
        random_restaurant = df.iloc[random.randint(0, len(df)-1)]
        
        return render_template('index.html', restaurant=random_restaurant)
    except Exception as e:
        # Return the error message for debugging
        return f"An error occurred: {str(e)}", 500

# Add any other routes you had here