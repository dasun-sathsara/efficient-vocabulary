import typer
from random import choice
from typing import Optional


def get_greeting() -> str:
    return choice(["Hello", "Hola", "Howdy"])


# * optional CLI argument
def main(
    first_name: str = typer.Argument(..., help="first name of the user", metavar="First Name"),
    last_name: str = typer.Argument("", help="last name of the user", metavar="[Last Name]", rich_help_panel="Optional Arguments"),
    greeting: str = typer.Argument(
        get_greeting,
        help="random greeting will be selected if not set",
        show_default="random greeting",
        rich_help_panel="Optional Arguments",
    ),
):
    print(f"{greeting}, {first_name} {last_name}!")


if __name__ == "__main__":
    typer.run(main)
