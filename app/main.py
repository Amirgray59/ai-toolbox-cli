
from fastapi import FastAPI 

import os 
from redis import Redis 

app = FastAPI() 

REDIS_HOST= os.getenv("REDIS_HOST") 
REDIS_PORT= int(os.getenv("REDIS_PORT"))  
REDIS_ENCODE= bool(int(os.getenv("REDIS_ENCODE"))) 

redis = Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    encoding=REDIS_ENCODE
)

@app.get("/")
def main() : 
    return {"status" : "working"}


@app.get("/health")
def health() : 
    return {"status" : "ok"} 



@app.get("/counter")
def counter():
    value = redis_client.incr("counter")

    return {
        "counter": value
    }