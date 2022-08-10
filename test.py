from fastapi import FastAPI
from fastapi.responses import UJSONResponse,HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
from starlette.requests import Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')
data = requests.get("https://serverless-api.bell23bella.workers.dev/").json()
results = data['results']
#name = results[2]["properties"]["name"]["title"][0]["plain_text"]

@app.get("/")
async def say_helloworld():
    return "hello world"

@app.get("/items/1", response_class=UJSONResponse)
async def read_items():
    name = results[2]["properties"]["name"]["title"][0]["plain_text"]
    return name

def generate_html_response():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Work from Seoul</title>
    </head>

    <body>
        <h1>Work from Seoul</h1>
        {% for name in name %}
        <h2> {{ name }}</h2>
        {% endfor %}
        <h3></h3>
        <h3></h3>
        <h4></h4>
        
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/cafe", response_class=HTMLResponse)
async def read_items(request:Request, name: str):
    return generate_html_response({"request":request, "name":name})