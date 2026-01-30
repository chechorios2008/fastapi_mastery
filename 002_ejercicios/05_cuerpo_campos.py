from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()


Money = Annotated[float, Field(gt=0, description="El monto debe ser mayor a cero")]
CurrencyCode = Annotated[str, Field(pattern=r"^[A-Z]{3}$", examples=["USD", "EUR", "COP"])]
TransactionNote = Annotated[str, Field(min_length=5, max_length=50, title="Concepto de pago")]

class BankTransfer(BaseModel):
    # Aplicamos los tipos anotados al modelo
    amount: Money
    currency: CurrencyCode
    concept: TransactionNote

    # Añadir información adicional para la documentación (Swagger UI)
    is_international: bool = Field(
        default=False, 
        description="Indica si la cuenta destino es de un banco extranjero"
    )


@app.post("/transfer")
async def create_transfer(
    # Usamos Body para indicar que este modelo viene en el JSON de la petición
    transfer: Annotated[BankTransfer, Body(embed=True)]
):
    return {"message": "Transferencia procesada con éxito", "data": transfer}

# Ejemplo 2.0 


# Definición de un tipo reutilizable con validación estricta
MontoPositivo = Annotated[float, Field(gt=0, description="El valor debe ser estrictamente mayor a cero")]

class Transaccion(BaseModel):
    # Uso de Field para validación y metadatos adicionales
    cuenta_origen: str = Field(min_length=10, max_length=10, pattern=r"^\d+$")
    monto: MontoPositivo
    concepto: Annotated[str | None, Field(max_length=50)] = None