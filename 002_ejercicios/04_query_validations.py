from typing import Optional, Annotated, List
from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/transactions/search/")
async def search_transactions(
    # 1. Validación de String con min/max length
    q: Annotated[
        Optional[str],
        Query(
            min_length=3,
            max_length=50,
            title="Búsqueda de concepto",
            description="Busca transacciones por descripción"
        )
    ] = None, 
    # 2. Parámetro REQUERIDO con Expresión Regular (Regex)
    # Formato esperado: ABC123456
    user_code: Annotated[
        str,
        Query(pattern="^[A-Z]{3}\\d{6}$")
    ] = ...,  # El '...' indica que es obligatorio
    # 3. Lista de parámetros (Múltiples valores en la URL)
    # URL: ?tags=salud&tags=hogar
    tags: Annotated[
        List[str],
        Query(title="Categorias de gasto")
    ] = []
):
    results = {
        "user_code": user_code,
        "filters": {"qury": q, "categories": tags}
    }
    return results