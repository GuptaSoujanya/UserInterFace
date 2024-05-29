from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr, BaseModel

from routes.route import router

app = FastAPI()

app.include_router(router)

app.mount("/static", StaticFiles(directory="LogingPage"), name="static")

templates = Jinja2Templates(directory= 'LogingPage')

@app.get("/" , response_class= HTMLResponse)
async def root(request : Request):
    return templates.TemplateResponse(
        request = request,name="Index.html"
    )
    
# @app.post("/submit")
# async def submit(username :str = Form(...) ,password : str = Form(...)):
#     return{username : password}

    