from pathlib import Path
from datetime import datetime

def save_words(name: str, words: set) -> None:
    """Save words to a new text file in data directory with current date

    Args:
        name (str): Movie or TV show name
        words (set): vocabulary words
    """

    file_name = f'{name}|{datetime.now().timestamp}'

    ...
