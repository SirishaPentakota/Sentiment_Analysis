from flask import Flask, render_template, request
from textblob import TextBlob

# Creating flask instance
app = Flask(__name__)

# Home page flask code
@app.route('/')
def home():
    return render_template('home.html')

# Prediction page flask code
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['text']
    
    # Analyzing sentiment using TextBlob
    blob = TextBlob(message)
    sentiment_score = blob.sentiment.polarity

    return render_template('result.html', prediction=sentiment_score, msg=message)

# Running the flask app
if __name__ == '__main__':
    app.run(debug=True)
