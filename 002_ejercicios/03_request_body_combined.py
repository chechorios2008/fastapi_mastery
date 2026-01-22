# Este ejemplo integra la lógica de Pydantic body, path y query

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 


app = FastAPI()


# Definición del esqueda de los datos. 
class UserUpdate(BaseModel):
    phone: str
    address: str
    email: Optional[str] = None

@app.put("/users/{user_id}")
async def update_user_profile(
    user_id: int, 
    user_data: UserUpdate,
    send_sms: bool = False
):
    """"Simulación de la actualización de la data"""
    response = {
        "message": f"Perfil del usuario {user_id} actualizado.",
        "updated_data": {
            "sms_sent": send_sms
        }   
    }
    if send_sms:
        print(f"Enciando sms al numero: {user_data.phone}")

    return response