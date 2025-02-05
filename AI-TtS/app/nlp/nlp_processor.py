import nltk
from nltk.corpus import stopwords

nltk.download('stopwords',quiet=True)

def clean_text(text):
    stop_words = set(stopwords.words('turkish')) #Enter the code of the language you want it to stop when it encounters a word in another language, e.g. turkish
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(cleaned_words)
