from fastapi import FastAPI

app=FastAPI()


@app.get("/multiply/{a}/{b}")
def multyply(a:int,b:int):
    return {a*b}

def add(ab,f):
    return {"Fahad"}
def asylum(shear_brute):
    return ("We must endure the")








