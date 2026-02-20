from fastapi import FastAPI

app=FastAPI()


@app.get("/multiply/{a}/{b}")
def multyply(a:int,b:int):
    return {a*b}








