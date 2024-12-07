from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
import pandas as pd
import os
from maquillaje import venta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

app.include_router(venta)

# Configuración para los templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tipo", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("TipoDatos.html", {"request": request})

@app.get("/datawrapper", response_class=HTMLResponse)
async def get_datawrapper(request: Request): 
    return templates.TemplateResponse("DataWrapper.html", {"request": request})

@app.get("/python", response_class=HTMLResponse)
async def get_datawrapper(request: Request): 
    return templates.TemplateResponse("Python.html", {"request": request})

@app.get("/r", response_class=HTMLResponse)
async def get_datawrapper(request: Request): 
    return templates.TemplateResponse("R.html", {"request": request})

@app.get("/read-csv/")
async def read_csv():
    # Construir la ruta completa del archivo
    file_path = os.path.join("static", "tienda_maquillaje.csv")
    
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="El archivo no se encuentra.")

    # Leer el archivo CSV con pandas
    try:
        df = pd.read_csv(file_path)
        return {
            "columns": df.columns.tolist(),
            "rows": df.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el archivo: {str(e)}")

@app.get("/datos", response_class=HTMLResponse)
async def get_datawrapper(request: Request):
    # Llamar a la función que lee el CSV
    data = await read_csv()

    # Pasar los datos a la plantilla
    return templates.TemplateResponse("datos.html", {
        "request": request,
        "columns": data["columns"],
        "rows": data["rows"]
    })
