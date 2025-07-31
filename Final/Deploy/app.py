from flask import Flask, render_template, request
import joblib
import re
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

# Load the model and vectorizer
vectorizer = joblib.load('tfidf_vectorizer.joblib')
clf = joblib.load('logreg_model.joblib')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'http\S+|www\S+', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 2]
    return ' '.join(tokens)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        input_text = request.form['text']
        clean_text = preprocess_text(input_text)
        X_input = vectorizer.transform([clean_text])
        pred = clf.predict(X_input)[0]
        prediction = pred
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
