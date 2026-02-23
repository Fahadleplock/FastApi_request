from fastapi import FastAPI
from pydantic import BaseModel



app=FastAPI()
class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    return {"sended_name":user.name,"sended_age":user.age}
   




    
 









