#uvicorn api:app --port 8000 --reload
from fastapi import APIRouter, Path, Request
from model import Venta
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates/")
  
venta_list:Venta = []
venta = APIRouter()

@venta.post("/ventas")
def add_todo(venta:Venta):
    venta_list.append(venta)
    return {"message":"Added"}


@venta.get("/venta")
def show_ventas():
    return {"ventas":venta_list}

@venta.get("/venta/{venta_id}")
def show_one_venta(venta_id:int=Path(...,title="ID")):
    for venta in venta_list:
        if venta.id == venta_id:
            return {"venta":venta}
    return {"message": "ID doesn't exist"}