from datetime import datetime
from uuid import UUID, uuid4
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

# Simulación de una base de datos. 
fake_db = {}


class CoffeeOrder(BaseModel):
    id: UUID
    customer: str
    created_at: datetime
    price: float

@app.post("/orders/")
async def create_order(order: CoffeeOrder):
    # 1. Si imprimimos 'order' es un objeto pydantic
    # CoffeeOrder(id=UUID('...'), created_at=datetime.datetime(...))
    print(f"Objeto original: {type(order)}")

    # 2. Convertimos a algo compatible con JSON
    # Esto transforma el UUID en str y el datetime en str (ISO format)
    json_data = jsonable_encoder(order)

    print(f"Objeto codificado: {type(json_data)}")
    print(f"Fecha codificada: {json_data['created_at']} (es un {type(json_data['created_at'])})")

    # 3. Ahora es seguro guardarlo en nuestra "DB" o enviarlo a otro servicio
    fake_db[str(order.id)] = json_data

    return {"status": "Guardado exitosamente", "data": json_data}
