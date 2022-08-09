from fastapi import FastAPI
from starlette.requests import Request
import requests
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

data = requests.get("https://serverless-api.bell23bella.workers.dev/").json()

results = data['results']
properties = results[0]["properties"]
templates = Jinja2Templates(directory='templates')

@app.get("/data/3")
def geturl1():
    return results[2]["properties"]["name"]["title"][0]["plain_text"]

@app.get("/data/2")
def geturl1():
    return results[1]["properties"]


@app.get("/data/1")
def geturl1():
    return results[0]

@app.get("/data")
def geturl():
    return properties

@app.get("/")
def main():
    return FileResponse("templates/index.html")

