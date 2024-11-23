from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Read the CSV file
    df = pd.read_csv('data/RestaurantData.csv')
    
    # Get a random restaurant
    random_restaurant = df.iloc[random.randint(0, len(df)-1)]
    
    return render_template('index.html', restaurant=random_restaurant)

# Add any other routes you had here