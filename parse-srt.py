from pathlib import Path
import unicodedata

def parse_subtitle(fp: Path) -> list[str]:
    """Parse the .srt to file to extract text

    Args:
        fp (Path): Path object pointing to the subtitle file
    """
    with open(fp, "r") as f:
        lines = f.readlines()

    filtered_lines = []
    for line in lines:
        line: str = unicodedata.normalize("NFKC", line.strip())
        if not (line.isdigit() or "-->" in line):
            filtered_lines.append(line)


if __name__ == "__main__":
    sub = Path("Spider-Man_No_Way_Home.2022.1080p.Bluray.DTS-HD.MA.5.1.X264-EVO.srt")
    text = parse_subtitle(sub)
