import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from pathlib import Path
from parse_srt import parse_subtitle


def download_nltk_data() -> None:
    """Download required data for nltk"""

    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    nltk.download("averaged_perceptron_tagger")


def _get_words_nltk(words: list[str], ordered: bool = False, unique: bool = False) -> list[str]:
    """Extract a word list from the sentences and filter out stop words.
    Returns the lemmatized version of the word using parts of speech tagging.
    By default, for increased performance, returns an unordered list of words with no duplicates.

    Args:
        words (list[str]): Subtitle text as a list of strings
        ordered bool: If True, returns a ordered list of words with duplicates
    """

    final_words = []
    lemmatized_words = []
    lemmatizer = WordNetLemmatizer()

    full_string = "\n".join(words)
    words = word_tokenize(full_string)

    # * filter our non alphabetic words
    words = list(filter(lambda x: x.isalpha(), words))

    tagged_words = nltk.pos_tag(words)

    for word_tag in tagged_words:
        word, tag = word_tag

        if tag.startswith("NN"):
            # * noun
            lemmatized_word = lemmatizer.lemmatize(word, "n")
        elif tag.startswith("JJ"):
            # * adjective
            lemmatized_word = lemmatizer.lemmatize(word, "a")
        elif tag.startswith("VB"):
            # * verb
            lemmatized_word = lemmatizer.lemmatize(word, "v")
        elif tag.startswith("RB"):
            # * adverb
            lemmatized_word = lemmatizer.lemmatize(word, "r")
        else:
            lemmatized_word = word

        # print(f"{word} ({tag}) -> {lemmatized_word}")
        lemmatized_words.append(lemmatized_word)

    # * remove `. ?` from words
    map(lambda x: x.lower().replace(".", "").replace("?", ""), lemmatized_word)

    if ordered:
        for lemmatized_word in lemmatized_words:
            if not lemmatized_word in stopwords.words("english"):
                final_words.append(lemmatized_word)
    else:
        final_words = list(set(lemmatized_words).difference(set(stopwords.words("english"))))

    return final_words


def get_words(subtitle_file: Path(), ordered: bool = False) -> list[str]:
    """Checks if the identified words are in the `all_words` file and filter out words that are in the `common_words` file.
     By default, for increased performance, returns an unordered a list of words with no duplicates.

    Args:
        subtitle_file (Path): Subtitle file
        ordered (bool, optional): If True, returns a ordered list with no duplicates. Defaults to False.
    """

    # * word list paths
    parent_path = Path(".").parent
    all_words_path = parent_path / "word_data" / "25k.txt"
    # all_words_path = parent_path / "word_data" / "all_words.txt"
    common_words_path = parent_path / "word_data" / "common_words.txt"

    all_words = all_words_path.read_text().split("\n")
    common_words = common_words_path.read_text().split("\n")

    if ordered:
        word_list = parse_subtitle(subtitle_file)
        lemmatized_words = _get_words_nltk(word_list, ordered=True)
        final_filtered_words = []

        # * main filtering
        for lemmatized_word in lemmatized_words:
            if (
                (lemmatized_word in all_words)
                and (not lemmatized_word in common_words)
                and (not lemmatized_word in final_filtered_words)
            ):
                final_filtered_words.append(lemmatized_word)

    else:
        word_list = parse_subtitle(subtitle_file)
        lemmatized_words = _get_words_nltk(word_list)

        # * main filtering
        final_filtered_words = list(set(lemmatized_words).intersection(set(all_words)).difference(set(common_words)))

    # * filtering out words that are shorter than 3 letters
    final_filtered_words = list(filter(lambda x: len(x) > 2, final_filtered_words))

    return final_filtered_words


def get_words_with_frequency(words: list[str], sorted: bool = True):
    ...


if __name__ == "__main__":
    import parse_srt

    parent_path = Path(".").parent
    subtitle = parent_path / "subtitles" / "sample_subtitle.srt"

    a = get_words(subtitle, ordered=True)

    for i in range(len(a)):
        print(a[i])

        if i == 100:
            break

    # # a = get_words(get_words_nltk())
    # subtitle_list = parse_srt.parse_subtitle(subtitle)
    # nltk_words = _get_words_nltk(subtitle_list)
    # final_filtered = get_words(nltk_words)

    # print(len(final_filtered))
    # for j in final_filtered:
    #     print(j)

    # print(len(a))
    # print(a)
