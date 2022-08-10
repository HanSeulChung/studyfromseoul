from fastapi import FastAPI
from starlette.requests import Request
import requests
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

data = requests.get("https://serverless-api.bell23bella.workers.dev/").json()

results = data['results']
properties = results[0]["properties"]
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
name = results[2]["properties"]["name"]["title"][0]["plain_text"]

#cafename = results[i]["properties"]["name"]["title"][0]["plain_text"]
#cafeaddress = results[i]["properties"]["address"]["rich_text"][0]["text"]["content"]
#cafeurl = results[i]["properties"]["url"]["url"]
#cafetype = results[i]["properties"]["type"]["rich_text"][0]["text"]["content"]

class Cafe(BaseModel):
    name :str
    address : str
    type : str
    url : str

@app.get("/data/5")
def geturl1():
    return name
@app.get("/data/4")
def geturl1():
    return results[2]["properties"]["name"]["title"][0]["plain_text"]
@app.get("/data/3")
def geturl1():
    return results[2]["properties"]["address"]["rich_text"][0]["text"]["content"]
@app.get("/data/2")
def geturl1():
    return results[2]["properties"]["url"]["url"]
@app.get("/data/1")
def geturl():
    return results[2]["properties"]["type"]["rich_text"][0]["text"]["content"]

@app.get("/",response_class=HTMLResponse)
def main(request: Request, cafe :Cafe):
    return templates.TemplateResponse("index.html", {"request": request, "cafe": cafe})

