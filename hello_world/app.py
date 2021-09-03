import os

from fastapi import FastAPI, Request
from mangum import Mangum

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix)  # Here is the magic

templates = Jinja2Templates(directory="templates")


@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}



@app.get("/webapp/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


handler = Mangum(app)
