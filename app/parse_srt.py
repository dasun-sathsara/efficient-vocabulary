from pathlib import Path
import unicodedata


def parse_subtitle(fp: Path) -> list[str]:
    """Parse the .srt to file and extract text

    Args:
        fp (Path): Path object pointing to the subtitle file
    """
    lines = fp.read_text().split('\n') 

    filtered_lines = []
    for line in lines:
        line: str = unicodedata.normalize("NFKC", line.strip())
        if not (line.isdigit() or "-->" in line):
            filtered_lines.append(line)

    return filtered_lines


if __name__ == "__main__":
    sub = Path("sample_subtitle.srt")
    text = parse_subtitle(sub)
    print(text)
