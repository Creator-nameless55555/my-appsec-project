import typer
from typing import Optional

app = typer.Typer(help="Утилита для приветствия в стиле AppSec.")

def build_message(name: str, lastname: str, formal: bool) -> str:
    """Формирует строку приветствия."""
    if formal:
        return f"Добрый день, {name} {lastname}!"
    return f"Привет, {name}!"

@app.command()
def main(
    name: str = typer.Argument(..., help="Имя пользователя"),
    lastname: Optional[str] = typer.Option("", "--last", help="Фамилия"),
    formal: bool = typer.Option(False, "--formal", "-f", help="Официальный стиль")
):
    message = build_message(name, lastname, formal)
    typer.echo(message)

if __name__ == "__main__":
    app()
