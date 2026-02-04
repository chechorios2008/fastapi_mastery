from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field


app = FastAPI()


# 1. Excepcion personalizada. 
class InsufficientFundsException(Exception):
    def __init__(self, amount_requested: float, balance: float):
        self.amount_requested = amount_requested
        self.balance = balance


# 2. Controlador para excepciones personalizadas. 
@app.exception_handler(InsufficientFundsException)
async def funds_exception_handler(request: Request, exc: InsufficientFundsException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Fondos Insuficientes",
            "mensaje": f"Intentaste retirar {exc.amount_requested}, pero solo tiene {exc.balance}"
            "codigo_error": "BANK_001"
        }
    )


# 3. Manejador de errores. 
@app.exception_handler(RequestValidationError):
async def validator_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "detalle_tecnico": exc._errors(),
            "mensaje_usuario": "Los datos enviados son incorrectos"
        }
    )

class Withdrawal(BaseModel):
    amount: float = Field(gt=0)

# >>>> RUTAS <<<<

@app.post("/withdraw")
async def withdraw_money(data: Withdrawal): 
    current_balance = 50.0 # Simulación del balance
    
    # Uso HTTPException con encabezador personalizados. 
    if data.amount > 1000:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Limite diario de retiros excedido",
            headers={"X-Security-level": "High"}
        )

    # Uso de excepcion personalizada. 
    if data.amount > current_balance:
        raise InsufficientFundsException(amount_requested=data.amount, balance=current_balance)

    return {"message": "Retiro exitodo", "new_balance": current_balance - data.amount }

'''
Estrategia de Manejo de Errores
HTTPException: Úsala para errores esperados en el flujo normal (404, 401).
Global Handlers: Úsalos para "limpiar" el código. En lugar de usar try/except en cada ruta, lanza una 
excepción y deja que el handler la capture.

Validation Override: Es clave para internacionalizar (traducir) los errores que Pydantic genera 
automáticamente.

Status Codes: Usa siempre el módulo status de FastAPI (status.HTTP_404_NOT_FOUND) en lugar de números 
mágicos (404) para mayor claridad.
'''