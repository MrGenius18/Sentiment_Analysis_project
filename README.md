<h1 align="center">😊 Sentiment Analysis 😡</h1>

<p align="center">
  <img src="https://github.com/MrGenius18/Sentiment_Analysis_project/blob/a0c9b5946667b6ed92db942fc1bfb20c7048e066/extra%20materials/emojis.jpeg">
</p>

---

This is a Flask-based web application for sentiment analysis. It takes user input in the form of text and predicts whether the sentiment is positive or negative using a trained classification model.

---

<h2 align="left">➡️ Visit the Application</h2>

[![Click Me](https://img.shields.io/badge/Click-Me-blue?style=for-the-badge)](https://sentiment-analysis-4j2h.onrender.com)

---

## Features

- Cleans and preprocesses user input text
- Uses TF-IDF vectorization
- Predicts sentiment using a trained machine learning model
- Web-based user interface

## Installation Requirements

1. Clone the repository:
   ```bash
   git clone https://github.com/MrGenius18/Sentiment_Analysis_project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sentiment_Analysis_project
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Place the `tfidf.pkl` and `clf_model.pkl` files in the project directory.
2. Download NLTK stopwords (if not already available):
   ```python
   import nltk
   nltk.download('stopwords')
   ```

## Running the App

Run the Flask application using:

```bash
python app.py
```

By default, the app runs on `http://127.0.0.1:5000/`.

## File Structure

```
├── app.py              # Main Flask application
├── templates
│   ├── index.html      # HTML template for UI
├── tfidf.pkl           # Pre-trained TF-IDF vectorizer
├── clf_model.pkl       # Trained classification model
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation
```

## Usage

1. Open `http://127.0.0.1:5000/` in your browser.
2. Enter a review or text input.
3. Click submit to get the sentiment prediction.

## Demo

![Movie Recommender System Screenshot](https://github.com/MrGenius18/Sentiment_Analysis_project/blob/a0c9b5946667b6ed92db942fc1bfb20c7048e066/extra%20materials/demo1.png)

---

## Contributing

If you want to contribute to this project, feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License.

