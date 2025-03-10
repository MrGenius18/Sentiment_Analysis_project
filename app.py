from flask import Flask, request, render_template
import os
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import pickle

tfidf = pickle.load(open('pkl files/tfidf.pkl', 'rb'))
clf_model = pickle.load(open('pkl files/clf_model.pkl', 'rb'))

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


# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if no PORT is provided
    app.run(host="0.0.0.0", port=port, debug=True)
