# Asincrono

### 1. ¿Qué es la Asincronía?
En el mundo real, la asincronía es la capacidad de iniciar una tarea y, mientras esperas a que termine, hacer otra cosa.
Síncrono (Bloqueante): Haces una fila en el banco. No puedes hacer nada más hasta que el cajero te atienda. Si el cajero se tarda, tú y todos los que están detrás están "congelados".
Asíncrono (No bloqueante): Vas a un restaurante y pides pizza. Te dan un zumbador (un ticket). Mientras la pizza se hornea, te sientas, revisas tu celular o hablas con amigos. No te quedas parado frente al horno.

### 2. ¿Qué es asyncio en Python?
Es la librería que permite que Python se comporte como el cliente de la pizzería. Python, por defecto, es síncrono (un solo hilo). asyncio introduce el Event Loop (Bucle de Eventos).
Event Loop: Es un director de orquesta que maneja todas las tareas. Si una tarea dice "estoy esperando una respuesta de la base de datos", el Event Loop la pausa y le da el turno a la siguiente tarea.
Corrutinas: Son funciones que definimos con async def. Son funciones que "tienen permiso" de ser pausadas.

### 3. Asincronía en FastAPI
FastAPI está construido sobre Starlette y Uvicorn, que son motores asíncronos nativos.
Cuando defines una ruta en FastAPI como async def, le estás diciendo al servidor: "Oye, si esta petición tarda porque está descargando un archivo o consultando la DB, no detengas a los demás usuarios. Atiende otras peticiones mientras esta termina".

### 4. ¿Cómo se utiliza? (Sintaxis básica)
Para usar asincronía necesitas dos palabras clave fundamentales:
async def: Declara que la función es una corrutina.
await: Se coloca antes de una operación que sabemos que va a tardar (como una consulta a la DB o una petición a otra API). Significa: "Espera aquí, pero deja que el Event Loop haga otras cosas".


### 1. Coroutines (Corrutinas)
Es el concepto más básico. Una corrutina es una función definida con async def.
- Analogía: Es una receta de cocina. Tener la receta no significa que la comida esté hecha; solo son las instrucciones de cómo hacerla.

- Comportamiento: Si llamas a una corrutina como una función normal (mi_funcion()), no se ejecuta. Solo te devuelve un "objeto corrutina". Para que "cobre vida", debe ser enviada al Event Loop (usando await o asyncio.run()).

### 2. Tasks (Tareas)
Una Task es lo que sucede cuando envuelves una corrutina para que el Event Loop la ejecute lo antes posible.
Analogía: Es cuando le entregas la receta al chef y él empieza a cocinar.
Comportamiento: Las Tasks se usan para programar corrutinas de forma concurrente. Al crear una Task, le dices a Python: "Empieza esto ya, y avísame cuando termines, pero mientras yo sigo con otra cosa".

### 3. Futures (Futuros)
Un Future es un objeto que representa un resultado que aún no existe, pero que existirá en el futuro.
Analogía: Es el ticket numerado que te dan en la pizzería. No es la pizza, pero es la promesa de que, cuando el zumbador suene, ese ticket se convertirá en una pizza.
Comportamiento: Normalmente, tú como programador de FastAPI no creas Futures manualmente. Los crean las librerías de bajo nivel (como el driver de la base de datos). Tú simplemente haces await sobre ellos.

