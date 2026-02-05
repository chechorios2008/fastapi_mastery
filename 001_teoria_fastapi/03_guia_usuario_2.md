## Codificador compatible con JSON

Hay algunos casos en los que es posible que necesites convertir un tipo de datos (como un modelo de Pydantic) a algo compatible con JSON (como un dict, list, etc.).
Por ejemplo, si necesita almacenarlo en una base de datos.
Para ello, FastAPI proporciona una jsonable_encoder()función.

En Python, tenemos objetos complejos como datetime, UUID, o incluso los modelos de Pydantic. El problema es que el estándar JSON no sabe qué es un objeto datetime. JSON solo entiende de:
- Objetos (diccionarios)
- Arreglos (listas)
- Cadenas de texto (strings)
- Números, booleanos y null
jsonable_encoder toma un objeto de Python (como tu modelo Pydantic o una fecha) y lo convierte en algo "compatible con JSON" (un diccionario donde las fechas ya son strings, los UUID son strings, etc.).

🧩 jsonable_encoder
Es una utilidad de FastAPI que convierte objetos complejos de Python en tipos de datos primitivos compatibles con JSON.
- ¿Qué hace? Transforma datetime → str, UUID → str, set → list, etc.
- Diferencia con .dict(): Mientras que .dict() de Pydantic crea un diccionario pero mantiene los objetos como datetime, jsonable_encoder se asegura de que todo el contenido sea serializable a texto JSON.
- Uso principal: Preparar datos para ser guardados en bases de datos (especialmente NoSQL) o para ser procesados por librerías externas que no conocen Pydantic.
