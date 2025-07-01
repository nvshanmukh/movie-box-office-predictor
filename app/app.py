from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

model = pickle.load(open('model_movies.pkl', 'rb'))
scaler = pickle.load(open('scaler_movies.pkl', 'rb'))

genre_map = {
    'Action': 1,
    'Adventure': 2,
    'Comedy': 3,
    'Drama': 4,
    'Thriller': 5,
    'Science Fiction': 6,
    'Romance': 7,
    'Horror': 8,
    'Family': 9,
    'Animation': 10
}

director_map = {
    'James Cameron': 1,
    'Steven Spielberg': 2,
    'Christopher Nolan': 3,
    'Peter Jackson': 4,
    'Ridley Scott': 5,
    'Michael Bay': 6,
    'Quentin Tarantino': 7,
    'Tim Burton': 8,
    'Clint Eastwood': 9,
    'Zack Snyder': 10
}

@app.route('/')
def home():
    return render_template('Demo2.html')  

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_values = request.form

        genre_str = form_values['genres'].strip()
        director_str = form_values['director'].strip()

        genre_code = genre_map.get(genre_str, 0)
        director_code = director_map.get(director_str, 0)

        budget = float(form_values['budget'])
        popularity = float(form_values['popularity'])
        runtime = float(form_values['runtime'])
        vote_average = float(form_values['vote_average'])
        vote_count = float(form_values['vote_count'])
        release_month = int(form_values['release_month'])
        release_dow = int(form_values['release_DOW'])

        final_input = [[
            budget, genre_code, popularity, runtime,
            vote_average, vote_count, director_code,
            release_month, release_dow
        ]]

        print("Raw input:", final_input)
        scaled_input = scaler.transform(final_input)
        print("Scaled input:", scaled_input)

        log_prediction = model.predict(scaled_input)
        print("Log scale prediction:", log_prediction[0])

        try:
            revenue = log_prediction[0]
            if np.isinf(revenue) or revenue > 1e12:
                revenue = "Prediction too large or unrealistic input"
            else:
                revenue = f"${revenue:,.2f}"
        except Exception as e:
            revenue = f"Error in prediction: {str(e)}"


        return render_template('resultnew.html', prediction=revenue)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
   
    app.run(debug=True, use_reloader=True)
