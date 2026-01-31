from uuid import UUID, uuid4
from datetime import datetime
from typing import Annotated
from decimal import Decimal
from fastapi import FastAPI, Path, Query, Body, Header, Cookie, HTTPException
from pydantic import BaseModel, Field, EmailStr

'''
Este ejemplo simula el sistema de una Tienda de Café Especialidad. El objetivo es consolidar y afianzar
el estudio en los temas:
Parametros de ruta, parametros de consulta, cuerpo de la solicitud, validaciones de canedas y numeros, 
modelos de parametros de consulta, Cookies, parametros de encavezado, modelos de respuesta.
'''

app = FastAPI(title="Coffee Shop Mastery API")


# --- 1. MODELOS (Estructura del Dato / ADN) ---

class CoffeeOrder(BaseModel):
    """Modelo para recibir el pedido (Cuerpo de la solicitud)"""
    coffee_name: str = Field(min_length=3, max_length=50, examples=["Capuccino Vainilla"])
    cups: int = Field(gt=0, le=10, description="Cantidad de tazas en el pedido")
    sweetness_lavel: Annotated[int, Field(ge=0, le=5)] = 3
    is_iced: bool = False


class OrderResponse(BaseModel):
    """Modelo de respuesta (Filtrado de salida)"""
    order_id: UUID
    status: str = "En preparación"
    total_price: Decimal
    timestamp: datetime

# --- 2. TIPOS REUTILIZABLES (Annotated) ---


OrderIdPath = Annotated[UUID, Path(title="El ID unico del pedodo")]
UserAgentHeader = Annotated[str | None, Header(description="Detectar desde qué dispositivo piden")]
SessionCookie = Annotated[str | None, Cookie(description="Token de sesión del cliente")]

# --- 3. RUTA INTEGRADORA ---

@app.post(
    "/orders/{order_id}/confirm",
    response_model=OrderResponse,
    tags=["Pedidos"]
)

# Acción: Crear/Procesar una venta.
async def confirm_coffee_order(
    # Parametro de ruta
    order_id: OrderIdPath,
    # Cuerpo de la solicitud.
    order_data: CoffeeOrder,
    # Parámetro de Consulta (Query) - Para descuentos
    coupon: Annotated[str | None, Query(pattern=r"^COFFEE\d{3}$")] = None,
    # Parámetro de Encabezado (Header)
    user_agent: UserAgentHeader = None,
    # Parámetro de Cookie
    session_id: SessionCookie = None
):
    """
    Simula la confirmación de un pedido de café integrando todas las validaciones vistas.
    """

    # Lógica de negocio rápida
    price_per_cup = Decimal("4.50")
    total = price_per_cup * order_data.cups

    # Aplicar descuento si hay cupón
    if coupon:
        total -= Decimal("1.00")

    # Verificación de "sesión" ficticia
    if not session_id:
        print("Aviso: Pedido realizado por un invitado sin cookie de sesión.")

    # Retornamos un diccionario que FastAPI filtrará usando OrderResponse
    return {
        "order_id": order_id,
        "total_price": total,
        "timestamp": datetime.now(),
        "extra_info_hidden": "Esto no saldrá en el JSON por el response_model"
    }

# --- 4. RUTA DE CONSULTA (Parámetros de consulta múltiples) ---


@app.get("/orders/search")
async def search_orders(
    # Validaciones de números y cadenas en Query
    limit: Annotated[int, Query(gt=0, le=100)] = 10,
    category: Annotated[str, Query(min_length=3)] = "Calientes"
):
    return {"message": f"Buscando {limit} pedidos en la categoría {category}"}
