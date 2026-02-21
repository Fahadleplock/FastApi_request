from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
import asyncio
import time


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


async def george(a,b):
    await time.sleep(6)
    return (a+b)

async def get():
 









