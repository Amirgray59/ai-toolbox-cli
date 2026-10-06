
from fastapi import FastAPI 

app = FastAPI() 


@app.get("/")
def main() : 
    return {"status" : "working"}


@app.get("/health")
def health() : 
    return {"status" : "ok"} 