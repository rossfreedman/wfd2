from flask import Flask, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Use the absolute path we now know works
        csv_path = os.path.join(os.getcwd(), 'data', 'RestaurantData.csv')
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Get a random restaurant
        random_restaurant = df.iloc[random.randint(0, len(df)-1)]
        
        # For debugging, first let's just return the restaurant data
        return str(random_restaurant)  # We'll change this to render_template once we confirm it works
        
    except Exception as e:
        return f"Debug Error: {str(e)}", 500

# Add any other routes you had here