import typer
from typing import List, Optional
app = typer.Typer()

@app.command()
def sum_int(numbers: List[int] = typer.Argument(None),
        input: Optional[str] = typer.Option(None, '-f'),
        output: Optional[str] = typer.Option(None, '-o')):
    total_sum = 0
    if numbers:
        total_sum += sum(numbers)
    
    if input:
        with open(input, 'r') as f:
            for line in f:
                total_sum += int(line.strip())

    if output:
        with open(output, 'w') as f:
            f.write(str(total_sum))
    else:
        print(total_sum)

if __name__ == "__main__":
    app()