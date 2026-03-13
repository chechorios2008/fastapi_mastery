import asyncio
import time

# 1. COROUTINE (La receta): Definida con 'async def'
async def preparar_cafe(nombre_cliente, tiempo_preparacion):
    print(f"☕ [MESERO] Tomando pedido de {nombre_cliente}...")
    
    # Aquí ocurre la magia del AWAIT: 
    # El mesero no se queda mirando la cafetera, suelta el control.
    await asyncio.sleep(tiempo_preparacion) 
    
    print(f"✅ [COCINA] Café de {nombre_cliente} listo tras {tiempo_preparacion}s.")
    return f"Café para {nombre_cliente}"

async def main():
    print("--- INICIO DE JORNADA ASÍNCRONA ---")
    start_time = time.perf_counter()

    # 2. TASKS (Los pedidos en vuelo):
    # 'create_task' pone la corrutina a funcionar de inmediato en el Event Loop.
    print("📢 [MESERO] Recibiendo pedidos de Juan y Maria...")
    tarea_juan = asyncio.create_task(preparar_cafe("Juan", 3))   # Tarea larga
    tarea_maria = asyncio.create_task(preparar_cafe("Maria", 1)) # Tarea corta

    # Mientras el café se hace (en el await de arriba), el programa SIGUE aquí.
    print("📢 [MESERO] Limpiando mesas mientras sale el café...")
    await asyncio.sleep(0.5) 
    print("📢 [MESERO] Atendiendo a otro cliente rápido...")

    # 3. FUTURES (El resultado esperado):
    # 'await' sobre la tarea es esperar a que el ticket se convierta en café real.
    # Maria terminará primero aunque su tarea se creó después de la de Juan.
    resultado1 = await tarea_juan 
    resultado2 = await tarea_maria

    end_time = time.perf_counter()
    print(f"\nResultados: {resultado1} y {resultado2}")
    print(f"--- FIN: Todos servidos en {end_time - start_time:.2f} segundos ---")

if __name__ == "__main__":
    # Punto de entrada para ejecutar la corrutina principal
    asyncio.run(main())