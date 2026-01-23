### Definiciones:
- En software, un esquema es una definición abstracta de cómo debe verse tu API: qué rutas tiene, qué datos recibe (un número, un texto) y qué devuelve.

- OpenAPI es un estándar internacional (un lenguaje común) para describir APIs REST.

- OpenAPI => Antes, cada programador documentaba su API como quería (en un Word, en un Excel, o no lo hacía). OpenAPI es un estándar internacional (un lenguaje común) para describir APIs REST.

## Parámetros de ruta

Path Parameters: Son variables que forman parte de la URL. Se definen en FastAPI usando llaves {}.

## Cuerpo de la solicitud

El Path es el "A quién" o "A dónde".
El Body es el "Qué" o "Cómo".
Para la validación de datos se utiliza "Pydantic" https://docs.pydantic.dev/latest/

# "trinidad" de la comunicación en una API.
### body, path y query

1. El Concepto aplicado al ATM
Path Parameter (user_id): Identifica quién es el usuario. Es parte de la URL porque el recurso (el usuario) ya existe en el sistema.

Request Body (UserUpdate): Contiene la información sensible o compleja que se va a cambiar. Se envía "oculto" en el cuerpo de la petición.

Query Parameter (confirm): Es un filtro o bandera opcional. En este caso, lo usaremos para preguntar si queremos que el sistema envíe un SMS de confirmación tras el cambio.

# Parámetros de Query y Validaciones de String

### 1. ¿Qué es Annotated y por qué usarlo?
- Anteriormente, FastAPI ponía las validaciones directamente en el valor por defecto del parámetro. La forma    moderna (desde Python 3.9+) es usar Annotated.

- Annotated es una funcionalidad de Python (introducida en la versión 3.9) que permite añadir metadatos a los tipos de datos sin cambiar el comportamiento del tipo en sí.

- Query es una clase de FastAPI que se utiliza para declarar validaciones y metadatos específicos para los parámetros de consulta (los que van después del ? en la URL).






