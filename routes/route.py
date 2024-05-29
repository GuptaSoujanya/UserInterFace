from fastapi import FastAPI, APIRouter, Form
from pydantic import EmailStr
from typing import Optional
from models.grtdata import CreateUser
from config.database import collection_name
from schema.schemas import list_serial


router = APIRouter()

# Get REQUEST METHOD

@router.get("/admin{token_id}")
async def get_data(token_id : Optional[str] =None):
    if(token_id != "2003"):
        return {"user is invalid"}
    
    user_data = list_serial(collection_name.find())
    return user_data

@router.post("/User_created")
async def create_user(name: str = Form(...), password: str = Form(...), email: EmailStr = Form(...)):
    user_data = {
        "name": name,
        "password": password,
        "email": email
    }
    collection_name.insert_one(user_data)
    return {"message": "User created successfully"}


@router.post("/submit")
async def find_user(username :str = Form(...) ,password : str = Form(...)):
    user_data = list_serial(collection_name.find({"name":username,"password":password}))
    if(user_data):
        return {"user is valid"}
    else:
        return {"user is invalid"}