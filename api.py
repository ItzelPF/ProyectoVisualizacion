from fastapi import FastAPI
from maquillaje import venta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

app.include_router(venta)

# Configuración para los templates
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static/"),name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
