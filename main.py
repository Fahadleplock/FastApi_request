from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

class User(BaseModel):
    name:str
    age:int
    email:EmailStr

app=FastAPI()


@app.get("/multiply/{a}/{b}")
def multyply(a:int,b:int):
    return {a*b}

def add(ab,f):
    return {"Fahad"}
def asylum(shear_brute):
    return ("We must endure the")
 









