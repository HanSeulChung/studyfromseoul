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



#cafename = results[i]["properties]["name"]["title"][0]["plain_text]
#cafeaddress = results[i]["properties"]["address"]["rich_text"][0]["text"]["content"]
#cafeurl = results[i]["properties"]["url"]["url"]
#cafetype = results[i]["properties"]["type"]["rich_text"][0]["text"]["content"]

@app.get("/data/3")
def geturl1():
    return results[2]["properties"]["name"]["title"][0]["plain_text"]
@app.get("/data/2")
def geturl1():
    return results[2]["properties"]["address"]["rich_text"][0]["text"]["content"]


@app.get("/data/1")
def geturl1():
    return results[2]["properties"]["url"]["url"]

@app.get("/data")
def geturl():
    return results[2]["properties"]["type"]["rich_text"][0]["text"]["content"]

@app.get("/")
def main():
    return results[2]["properties"]

