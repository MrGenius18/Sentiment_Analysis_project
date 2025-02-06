from flask import Flask, request, render_template

import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import pickle

tfidf = pickle.load(open('tfidf.pkl', 'rb'))
clf_model = pickle.load(open('clf_model.pkl', 'rb'))

nltk.download('stopwords')


app =Flask(__name__)


#################### Clean Review ###################
stop_word = set(stopwords.words("english"))
emoji_pattern = re.compile(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)')

def preprocessing(text):
    text = re.sub(r'<[^>]*>', '', text) # remove html tags
    emojis = emoji_pattern.findall(text)
    text = re.sub(r'[\W+]', ' ', text.lower()) + ' '.join(emojis).replace('-', '')

    peter = PorterStemmer()
    text = [peter.stem(word) for word in text.split() if word not in stop_word]

    return " ".join(text)
#####################################################


############## call index.html file #################
@app.route('/')
def index():
    return render_template("index.html")
#####################################################


################ Predict Sentiment ##################
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        review = request.form['text']
        
        cleaned_review = preprocessing(review)

        review_vector = tfidf.transform([cleaned_review])
        
        predicted_sentiment = clf_model.predict(review_vector)[0]

        return render_template('index.html', prediction=predicted_sentiment)
#####################################################


if __name__ == "__main__":
    app.run(debug=True)