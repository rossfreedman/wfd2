from flask import Flask, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        df = pd.read_csv('data/RestaurantData.csv')
        random_restaurant = df.sample(n=1).iloc[0].to_dict()
        
        # Return formatted HTML
        return f"""
        <h1>{random_restaurant['Restaurant Name']}</h1>
        <ul>
            <li>Cuisine: {random_restaurant['Cuisine']}</li>
            <li>Price: {'$' * random_restaurant['Price']}</li>
            <li>Takeout: {random_restaurant['Takeout']}</li>
            <li><a href="{random_restaurant['URL']}" target="_blank">View Menu</a></li>
        </ul>
        """
        
    except Exception as e:
        return f"Debug Error: {str(e)}", 500

# Add any other routes you had here

if __name__ == '__main__':
    app.run()