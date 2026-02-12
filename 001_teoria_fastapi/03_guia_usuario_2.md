## Codificador compatible con JSON - jsonable_encoder

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

## Body - Actualizaciones
para aplicar actualizaciones parciales deberías:
- (Opcionalmente) usar PATCH en lugar de PUT.
- Recuperar los datos almacenados.
- Poner esos datos en un modelo de Pydantic.
- Generar un dict sin valores por defecto del modelo de entrada (usando exclude_unset)

##### En el estándar REST, existen dos formas de actualizar un recurso:
1. PUT (Reemplazo Total): Se utiliza cuando quieres enviar el objeto completo para sobrescribir el existente. Si olvidas enviar un campo, este podría quedar vacío o volver a su valor por defecto.
2. PATCH (Actualización Parcial): Es más "quirúrgico". Solo envías los campos que quieres cambiar (por ejemplo, solo el email) y el resto del objeto permanece intacto.

- exclude_unset=True: Al convertir un modelo a diccionario (model_dump o dict), este parámetro le dice a Pydantic: "Solo incluye en el diccionario los campos que el usuario envió explícitamente en el JSON". Si no lo usas, Pydantic incluirá los valores por defecto de los campos omitidos.

🔄 Resumen: Actualizaciones con Body
- PUT: Reemplaza todo. Útil para consistencia total.
- PATCH: Actualiza solo lo necesario. Requiere que los campos del esquema sean opcionales.
- exclude_unset=True: Es la clave de las actualizaciones parciales. Evita que los valores por defecto del esquema Pydantic "pisen" los valores reales de la base de datos.
