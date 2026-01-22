1. async def: Le dice a FastAPI que la función puede realizar pausas para esperar algo.

2. await: Se coloca justo antes de la llamada que toma tiempo. Solo se puede usar dentro de funciones async.

3. Regla de Oro: Si tu código interactúa con una Base de Datos, una API externa o el sistema de archivos, lo más probable es que debas usar async.

# Las variables de entorno:
son valores que viven en el sistema operativo, fuera de tu código fuente.

- Seguridad: Nunca, bajo ninguna circunstancia, debes escribir contraseñas, llaves de API o secretos en tu código (esto se llama hardcoding). Si subes ese código a GitHub, cualquiera podría robar tus credenciales.

- Portabilidad: Permiten que el mismo código se comporte diferente si está en tu computadora (Desarrollo), en un servidor de pruebas (Testing) o atendiendo a clientes reales (Producción).

- Diferencia entre .env y el código: El .env es local y privado; el código es público.

- Pydantic Settings: Es la herramienta que FastAPI usa para "leer" el sistema de forma segura.

- Identificación (Path): Siempre para IDs o nombres únicos de recursos.

- Acción/Descripción (Body): Para objetos complejos (JSON). FastAPI sabe que es un Body porque usamos una clase que hereda de BaseModel.

- Modificación/Filtro (Query): Para parámetros que no son esenciales para identificar el recurso, pero que alteran cómo se ejecuta la función (paginación, filtros de fecha, confirmaciones).

- Combinación: FastAPI es capaz de distinguir cada uno automáticamente por el tipo de dato y la sintaxis:

Si está en la ruta {} -> Path.
Si es un tipo simple (int, str, bool) y no está en la ruta -> Query.
Si es un modelo Pydantic -> Body.