import typer
from rich import print

app = typer.Typer(help="LLM from scratch playground")

@app.command()
def hello(name: str = "world"):
    print(f"[bold green]hello[/bold green] {name}")

@app.command()
def train(steps: int = 10):
    print(f"Training for {steps} steps (stub)...")
    # TODO: call training.train.run(...)

@app.command()
def sample(prompt: str):
    print(f"Sampling from prompt: {prompt!r} (stub)...")
    # TODO: load model + generate tokens

if __name__ == "__main__":
    app()