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


# Registro Teórico: Programación Asíncrona con Bases de Datos
## Librería: aiosqlite

### 1. Definición
`aiosqlite` es un wrapper asíncrono para la librería estándar `sqlite3` de Python. Utiliza hilos internos para permitir que las operaciones de I/O (entrada/salida) de la base de datos no bloqueen el bucle de eventos (Event Loop) de la aplicación.

### 2. Por qué es necesaria en FastAPI
Por defecto, SQLite es síncrono. Si usamos `sqlite3` estándar dentro de una ruta `async def`, el servidor se detendrá por completo durante cada consulta. 
* **Problema:** Si una consulta tarda 2 segundos, la API no responderá a nadie más durante ese tiempo.
* **Solución:** Con `aiosqlite`, usamos `await db.execute(...)`, permitiendo que FastAPI atienda otras llamadas mientras la DB procesa la información.

### 3. Comparativa de Código

#### ❌ Síncrono (Bloqueante)
```python
import sqlite3

def get_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.execute("SELECT * FROM users") # El programa se detiene aquí
    return cursor.fetchall()

# 🛣️ APIRouter: Modularización en FastAPI

## 1. ¿Qué es un APIRouter?
En aplicaciones pequeñas, puedes poner todas tus rutas en el archivo `main.py`. Sin embargo, a medida que el proyecto crece (ej. gestión de usuarios, posts, pagos, notificaciones), el archivo se vuelve inmanejable.

`APIRouter` es una clase que permite definir rutas de forma aislada en archivos separados y luego "agruparlas" en la aplicación principal.



## 2. ¿Para qué sirve?
* **Organización:** Separa la lógica por dominios (Usuarios con usuarios, Posts con posts).
* **Reutilización:** Puedes definir configuraciones comunes para un grupo de rutas una sola vez.
* **Mantenimiento:** Facilita el trabajo en equipo, ya que diferentes programadores pueden trabajar en archivos distintos sin causar conflictos.

## 3. Anatomía de la Inclusión
Cuando usas `app.include_router()`, estás configurando tres elementos clave:

| Parámetro | Propósito | Ejemplo |
| :--- | :--- | :--- |
| **router** | El objeto router importado del archivo hijo. | `users.router` |
| **prefix** | Un camino de URL que se antepondrá a todas las rutas de ese archivo. | `/api/users` |
| **tags** | Etiquetas para agrupar las rutas en la documentación automática (/docs). | `["users"]` |

## 4. El Flujo de una Petición (Routing Table)
FastAPI no busca archivos en el disco duro cada vez que llega una petición. Al iniciar, construye una **Tabla de Rutas en memoria**:

1. **Registro:** `main.py` lee los archivos de los routers y llena su mapa.
2. **Matching:** Cuando llega una petición (ej. `GET /api/users/5`), FastAPI busca en su mapa cuál función coincide con esa **URL** y ese **Método HTTP**.
3. **Ejecución:** Salta directamente a la función correspondiente en el archivo donde fue definida.

## 5. Ejemplo de Estructura Profesional
```text
proyecto/
├── main.py          # Centralizador (Administrador)
├── database.py      # Conexión a DB
├── models.py        # Modelos de SQLAlchemy
├── schemas.py       # Modelos de Pydantic
└── routers/         # Carpeta de módulos (Barrios)
    ├── users.py
    └── posts.py
