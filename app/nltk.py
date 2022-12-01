import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def download_nltk_data() -> None:
    """Download required data for nltk"""

    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    nltk.download("averaged_perceptron_tagger")


def get_words_nltk(words: list[str]) -> list[str]:
    """Extract a word list from the sentences and filter out stop words.
    Returns the lemmatized version of the word using parts of speech tagging.

    Args:
        words (list[str]): Subtitle text as a list of strings
    """

    final_words = []
    lemmatizer = WordNetLemmatizer()

    full_string = "\n".join(words)
    words = word_tokenize(full_string)
    filtered_words = set(map(lambda x: x.lower().replace(".", "").replace("?", ""), words)).difference(set(stopwords.words("english")))
    tagged_words = nltk.pos_tag(filtered_words)

    for word_tag in tagged_words:
        word, tag = word_tag

        if tag.startswith("NN"):
            # noun
            lemmatized_word = lemmatizer.lemmatize(word, "n")
        elif tag.startswith("JJ"):
            # adjective
            lemmatized_word = lemmatizer.lemmatize(word, "a")
        elif tag.startswith("VB"):
            # verb
            lemmatized_word = lemmatizer.lemmatize(word, "v")
        elif tag.startswith("RB"):
            # adverb
            lemmatized_word = lemmatizer.lemmatize(word, "r")
        else:
            lemmatized_word = word

        # print(f"{word} ({tag}) -> {lemmatized_word}")
        final_words.append(lemmatized_word)

    return filtered_words
