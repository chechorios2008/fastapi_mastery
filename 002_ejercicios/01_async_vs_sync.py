from fastapi import FastAPI
import asyncio


app = FastAPI()

# Función Normal
@app.get("/procesar-calculo")
def calculo_pesado():
    # Esto bloquea a los demás usuarios hasta que termine
    resultado = sum(i * i for i in range(10_000_000))
    return {"resultado": resultado}


# Función Asíncrona (async def)
@app.get("/verificar-banco")
async def verificar_transaccion():
    # Simulamos una espera de base de datos o API externa de 2 segundos
    # 'await' le dice a Python: "puedes ir a atender a otro usuario mientras esto termina"
    await asyncio.sleep(2) 
    return {"status": "Transacción validada de forma asíncrona"}