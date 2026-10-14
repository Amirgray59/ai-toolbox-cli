from fastapi import FastAPI 
import os 
import typer 

app = typer.Typer()

tools = [] 


@app.command()
def main(
    name:str = typer.Argument("default naming"), 
    age: int = typer.Option(1, "--age", "-a", min=1, max=100), 
    uppercase: bool = typer.Option(False,  "--upercase-info", "-u")
) : 

    out = ["welcome", name]

    if age : 
        out.append(str(age))
    
    out = " ".join(out)

    if uppercase : 
        typer.echo(out.title())
    else : 
        typer.echo(out)

@app.command() 
def add(name: str) : 
    tools.append(name)

@app.command()
def list_tools() : 
    typer.echo(tools)


@app.command() 
def health() : 
    print(f"status ok") 



if __name__ == "__main__" : 
    app() 