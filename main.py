from fastapi import FastAPI
import requests
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
data = requests.get("https://serverless-api.bell23bella.workers.dev/").json()

results = data['results']
properties = results[0]["properties"]
templates = Jinja2Templates(directory='./')

@app.get("/data", response_class=HTMLResponse)
def geturl():
    return templates.TemplateResponse('index.html',{"properties":properties})

@app.get("/")
def main():
    return FileResponse("index.html")