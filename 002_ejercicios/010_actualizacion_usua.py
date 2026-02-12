from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()


# 1. Esquema para la Base de Datos (Simulada)
class UserInDB(BaseModel):
    id: int
    username: str
    email: str
    bio: str = "Sin biografía"
    is_active: bool = True


# 2. Esquema para PATCH (Todo es opcional)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    bio: Optional[str] = None
    is_active: Optional[bool] = None


# Base de datos ficticia
db_users = {
    1: UserInDB(id=1, username="checho", email="checho@gmail.com", bio="Python dev")
}


@app.patch("/users/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user_update: UserUpdate):
    # A. Buscar si existe el recurso
    stored_user_data = db_users.get(user_id)
    if not stored_user_data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # B. EL TRUCO MÁGICO: exclude_unset=True
    # Si el usuario solo envió {"bio": "Nueva bio"}, update_data solo tendrá esa llave.
    update_data = user_update.model_dump(exclude_unset=True)

    # C. Crear la copia actualizada del objeto almacenado
    updated_user = stored_user_data.model_copy(update=update_data)

    # D. Guardar en la "Base de datos"
    db_users[user_id] = updated_user

    return updated_user