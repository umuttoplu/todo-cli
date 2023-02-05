import click
import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo, undone_todo, get_undone_todos

console = Console()

app = typer.Typer()


@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()


@app.command(short_help='deletes given item')
def delete(position: int):
    typer.echo(f"deleting {position}")
    # indices in UI begin at 1, but in database at 0
    delete_todo(position - 1)
    show()


@app.command()
def update(position: int, task: str, category: str):
    typer.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    show()


@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position - 1)
    show()


@app.command()
def undone(position: int):
    typer.echo(f"undone {position}")
    undone_todo(position - 1)
    show(status=0)


@app.command(short_help='shows undone / all todos')
@click.option('--status', prompt='Status type',
              help="0 for undone, 1 for all", default=1)
def show(status: int = 1):
    if status == 0:
        tasks = get_undone_todos()
    else:
        tasks = get_all_todos()
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=5)
    table.add_column("Todo", min_width=25)
    table.add_column("Category", min_width=15, justify="right")
    table.add_column("Done", min_width=15, justify="right")

    def get_category_color(category):
        COLORS = {'Self-Learning': 'cyan',
                  'Watchlist': 'red',
                  'Tasks': 'cyan',
                  'Research': 'green',
                  'Personal': 'yellow',
                  'English': 'blue'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 1 else '❌'
        table.add_row(str(index), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()
