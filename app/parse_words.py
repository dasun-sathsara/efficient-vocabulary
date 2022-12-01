import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from pathlib import Path


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
            #* noun
            lemmatized_word = lemmatizer.lemmatize(word, "n")
        elif tag.startswith("JJ"):
            #* adjective
            lemmatized_word = lemmatizer.lemmatize(word, "a")
        elif tag.startswith("VB"):
            #* verb
            lemmatized_word = lemmatizer.lemmatize(word, "v")
        elif tag.startswith("RB"):
            #* adverb
            lemmatized_word = lemmatizer.lemmatize(word, "r")
        else:
            lemmatized_word = word

        # print(f"{word} ({tag}) -> {lemmatized_word}")
        final_words.append(lemmatized_word)

    return list(final_words)


def get_words(words: list[str]) -> list[str]:
    """Checks if the identified words are in the `all_words` file and filter out words that are in the `common_words` file"""

    #* paths
    parent_path = Path(".").parent
    all_words_path = parent_path / "word_data" / "25k.txt"
    # all_words_path = parent_path / "word_data" / "all_words.txt"
    common_words_path = parent_path / "word_data" / "common_words.txt"

    all_words = set(all_words_path.read_text().split("\n"))
    common_words = set(common_words_path.read_text().split("\n"))

    #* main filtering
    final_filtered_words = list(set(words).intersection(all_words).difference(common_words))

    #* filtering out words that are shorter than 3 letters
    final_filtered_words = filter(lambda x: len(x) > 2, final_filtered_words)

    return list(final_filtered_words)


if __name__ == "__main__":
    import parse_srt

    parent_path = Path(".").parent
    subtitle = parent_path / "subtitles" / "sample_subtitle.srt"

    # a = get_words(get_words_nltk())
    subtitle_list = parse_srt.parse_subtitle(subtitle)
    nltk_words = get_words_nltk(subtitle_list)
    final_filtered = get_words(nltk_words)

    print(len(final_filtered))
    for j in final_filtered:
        print(j)

    # print(len(a))
    # print(a)
