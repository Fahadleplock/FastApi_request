from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field,field_validator
import re
app=FastAPI()

class UserRegister(BaseModel):
    username:str=Field(...,min_length=5,max_length=15)
    email:EmailStr
    password:str
    age:int=Field(...,ge=18,le=100)
    @field_validator("password")
    @classmethod
    def validate_password(cls,value):
        if not re.search(r"\d",value):
            raise ValueError("Password must contain atleast 1 number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("password should contain ! special character")
        return value
@app.post("/register")
def register(user: UserRegister):
    return {
        "message": "User registered successfully",
        "user": user
    }    
        
        
        
        
        







    
 









