from flask import Flask, jsonify, request, render_template
import pandas as pd
import random
import os

app = Flask(__name__)

def load_all_options():
    try:
        df = pd.read_csv(os.path.join('data', 'RestaurantData.csv'))
        
        # Clean the data: Replace NaN with empty strings and convert to string type
        df = df.fillna('')
        for column in df.columns:
            df[column] = df[column].astype(str)
            
        # Convert to records and ensure all values are JSON serializable
        options = []
        for record in df.to_dict('records'):
            clean_record = {}
            for key, value in record.items():
                # Convert any remaining NaN strings to empty string
                if value.lower() == 'nan':
                    clean_record[key] = ''
                else:
                    clean_record[key] = str(value)  # Ensure all values are strings
            options.append(clean_record)
            
        print(f"Successfully loaded {len(options)} options from CSV")
        print("Sample option:", options[0] if options else "No options loaded")
        return options
        
    except Exception as e:
        print(f"Error loading RestaurantData.csv: {str(e)}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_choices', methods=['POST'])
def get_choices():
    try:
        data = request.json
        remaining = data.get('remaining', [])
        previous_survivor = data.get('previousSurvivor')
        
        # Load initial options if empty
        if not remaining:
            remaining = load_all_options()
            if not remaining:
                return jsonify({'error': 'Unable to load restaurant options'})
        
        print(f"Remaining options count: {len(remaining)}")
        
        # If we're down to one option, that's our winner
        if len(remaining) == 1:
            return jsonify({'winner': remaining[0]})
            
        # If we have a previous survivor, try to pair it with a similar cuisine
        if previous_survivor:
            survivor_cuisine = previous_survivor['Cuisine']
            
            # Get remaining options excluding the previous survivor
            available_options = [opt for opt in remaining 
                               if opt['Restaurant Name'] != previous_survivor['Restaurant Name']]
            
            # If no more options to compare against, previous survivor wins
            if not available_options:
                return jsonify({'winner': previous_survivor})
                
            # Try to find options with matching cuisine
            matching_cuisine_options = [opt for opt in available_options 
                                      if opt['Cuisine'].lower() == survivor_cuisine.lower()]
            
            # If we found matching cuisine options, use one of those
            if matching_cuisine_options:
                next_opponent = random.choice(matching_cuisine_options)
            else:
                # If no matching cuisine, use any available option
                next_opponent = random.choice(available_options)
            
            return jsonify({
                'choice1': previous_survivor,
                'choice2': next_opponent,
                'remaining': remaining,
                'matchingCuisine': bool(matching_cuisine_options)
            })
        else:
            # First comparison - get two random options
            choices = random.sample(remaining, 2)
            return jsonify({
                'choice1': choices[0],
                'choice2': choices[1],
                'remaining': remaining
            })
            
    except Exception as e:
        print(f"Error in get_choices: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
