from fastapi import FastAPI 
import os 
import typer 

app = typer.Typer()


@app.command()
def main(name:str) : 
    print(f"welcome {name}")


@app.command() 
def health() : 
    print(f"status ok") 



if __name__ == "__main__" : 
    app() 