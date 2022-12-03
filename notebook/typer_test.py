import typer


def main(input_file: str, output_file: str):
    """Copies the content of input_file to output_file"""
    if not input_file.endswith("txt"):
        print("Input file should be of type txt")
        raise typer.Abort(1)

    with open(output_file, "w", encoding="utf-8") as of:
        with open(input_file, "r", encoding="utf-8") as inputf:
            of.write(inputf.read())


if __name__ == "__main__":
    typer.run(main)
