import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def preprocess_text(text):
    sentences = sent_tokenize(text)
    cleaned_text = " ".join(sentences)
    return cleaned_text

# Example Usage
sample_text = "This is an example transcript. It has multiple sentences."
print(preprocess_text(sample_text))
