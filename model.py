from pydantic import BaseModel
from datetime import date

class Venta(BaseModel):
    id: int
    fecha: date
    producto: str
    marca: str
    categoria: str
    precio_unitario: float
    cantidad_vendida: int
    total_venta: float
    metodo_pago: str
    estado: str