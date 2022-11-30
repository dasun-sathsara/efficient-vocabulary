import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
s = word_tokenize(
    "Tokenizers divide strings into lists of substrings. For example, tokenizers can be used to find the words and punctuation in a string:."
)

print(s)
