import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):

    # convert to lowercase
    text = text.lower()

    # fix irregular spacing
    text = " ".join(text.split())

    # remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # tokenize
    words = text.split()

    # remove stopwords
    words = [word for word in words if word not in stop_words]

    cleaned_text = " ".join(words)

    return cleaned_text