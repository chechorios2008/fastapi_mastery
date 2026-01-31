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

## 📝 Apuntes: Cuerpo - Campos (Field) y Annotated

1. El rol de Field en los Modelos
Así como usamos Query, Path y Body para validar parámetros en las funciones de ruta, utilizamos pydantic.Field para declarar validaciones y metadatos dentro de las clases de Pydantic.

- Validación de datos: Permite restringir valores (mínimos, máximos, patrones regex).
- Anotación de metadatos: Añade títulos, descripciones y ejemplos que enriquecen la documentación automática (Swagger UI).
- Valores por defecto: Define el comportamiento inicial de un campo si no se recibe en el JSON.

2. La potencia de Annotated
La recomendación actual de FastAPI es utilizar Annotated para declarar estas validaciones.

¿Por qué usarlo? > Al usar Annotated, separamos el tipo de dato (ej. int, str) de los metadatos de validación (ej. Field). Esto hace que el código sea compatible con herramientas de análisis estático y mucho más fácil de leer.

### 🛠️ Capacidades de pydantic.Field
Con Field se puede controlar tres pilares fundamentales de tus datos:
1. Validación Estricta (Constraints)
Permite que Python detenga datos erróneos antes de que lleguen a tu lógica de negocio.
- Numéricos: Controlar rangos con gt (mayor que), ge (mayor o igual), lt (menor que) y le (menor o igual).
- Cadenas (Strings): Definir min_length, max_length y usar pattern (Regex) para formatos como emails, IDs o teléfonos.
- Colecciones: Validar el tamaño de listas con min_length y max_length.

2. Gestión de Metadatos y Documentación
Todo lo que escribas aquí se reflejará automáticamente en /docs (Swagger UI).
- title y description: Explica para qué sirve el campo.
- examples: Proporciona ejemplos reales para que otros desarrolladores prueben tu API fácilmente.
- alias: Útil cuando el JSON externo usa nombres que no siguen la convención de Python (ej: alias="Customer-ID" para la variable customer_id).
- deprecated: Marca campos que serán eliminados en versiones futuras sin romper la compatibilidad inmediata.

3. Comportamiento del Modelo
- default: Define un valor si el campo no se envía.
- default_factory: Para valores dinámicos (como una lista vacía list o la hora actual).
- exclude: Si quieres que un campo sea parte del modelo pero no se incluya en la respuesta JSON final (útil para contraseñas o datos internos).

#### ¿Cuándo usar cada uno?
- Path y Query: Se usan obligatoriamente cuando el dato NO es un objeto complejo (JSON), sino que viene suelto en la URL.
- Body: Se usa en la función de ruta para indicar que un parámetro debe leerse del cuerpo de la petición.
- Field: Se usa dentro de los modelos Pydantic.

## Tipos de datos adicionales

🚀 Tipos de Datos Adicionales

FastAPI/Pydantic convierten automáticamente formatos complejos de texto (JSON) a objetos Python reales.

- UUID: Es el estándar para identificadores únicos, seguros y distribuibles. Evita ataques de enumeración.
- Decimal: Debe usarse SIEMPRE para dinero. Los float en computación tienen errores de precisión (ej. 0.1 + 0.2 no siempre es 0.3).
- Timedelta/Datetime: Facilitan el manejo de zonas horarias y cálculos de expiración (ej. "Este token vence en 30 minutos").

#### ⚠️ Regla Financiera: float vs Decimal
- float: Úsalo para datos científicos, distancias o física, donde un error infinitesimal no importa.
- Decimal: Úsalo SIEMPRE para dinero, impuestos y contabilidad.
Nota técnica: Al enviar un Decimal a través de FastAPI, se recibe como un número en el JSON, pero Pydantic lo convierte internamente al objeto Decimal de Python para mantener la precisión durante los cálculos.

### 🍪 Cookies
⚠️ Regla Financiera: float vs Decimal
- float: Úsalo para datos científicos, distancias o física, donde un error infinitesimal no importa.
- Decimal: Úsalo SIEMPRE para dinero, impuestos y contabilidad.

Las cookies no son para enviar grandes volúmenes de datos, sino para identificadores persistentes.
- Sesiones de usuario: Guardar un session_id para saber quién está logueado sin pedir la contraseña en cada clic.
- Preferencias del cliente: Idioma preferido (español/inglés), tema (oscuro/claro).
- Seguimiento (Analytics): Identificar si un usuario es recurrente.

🍪 Parámetros de las Cookies
Las cookies permiten persistencia entre peticiones de forma automática por parte del navegador.
- Clase Cookie: Se usa para declarar parámetros que el cliente debe enviar en el encabezado Cookie.
- Uso de Annotated: Al igual que con Query, permite separar el tipo de dato de la validación del metadato.
- Limitación: Los navegadores limitan el tamaño de las cookies (generalmente 4KB), por lo que solo deben contener identificadores o configuraciones mínimas.

#### Importante
🔄 El Gran Paralelo: ¿Qué usar, cuándo y por qué?
##### 1. Path:
- ¿Qué es?: Parte de la URL fija.
- ¿Cuándo usarlo?: Para identificar un recurso específico.
- Ejemplo Real: /cuentas/{cuenta_id}

##### 2. Query:
- ¿Qué es?: Después del ? en la URL.
- ¿Cuándo usarlo?: Para filtrar, ordenar o buscar datos.
- Ejemplo Real: ?moneda=USD&limite=10

##### 3. Header:
- ¿Qué es?: Metadatos "invisibles".
- ¿Cuándo usarlo?: Seguridad, versiones, tokens o tipo de dispositivo.
- Ejemplo Real: X-API-Key, User-Agent

##### 4. Cookie:
- ¿Qué es?: Almacén en el navegador.
- ¿Cuándo usarlo?: Sesiones o preferencias que deben persistir solas.
- Ejemplo Real: session_id, dark_mode

##### 5. Body:
- ¿Qué es?: El objeto JSON.
- ¿Cuándo usarlo?: Para enviar mucha información o datos complejos.
- Ejemplo Real: Datos para crear un préstamo.

🚀 Dominando los Canales de Comunicación
Un experto en FastAPI sabe que:

- Path identifica el "QUÉ".
- Query define el "CÓMO" lo quiero ver.
- Header dice el "QUIÉN" o "DESDE DÓNDE" técnicamente.
- Body contiene el "CONTENIDO" pesado.

Tip de Oro: Usa siempre Annotated para todos estos. Mantiene tu código consistente y permite que herramientas como Pytest o MyPy entiendan mejor tu código.

### 🍪 Modelos de Cookies y Header

- Si tienes un grupo de cookies relacionadas, puedes crear un modelo de Pydantic para declararlas. 🍪
Esto le permitiría reutilizar el modelo en varios lugares y también declarar validaciones y metadatos para todos los parámetros a la vez. 😎

- Si tiene un grupo de parámetros de encabezado relacionados , puede crear un modelo de Pydantic para declararlos.
Esto le permitiría reutilizar el modelo en varios lugares y también declarar validaciones y metadatos para todos los parámetros a la vez. 😎
Puedes usar modelos de Pydantic para declarar encabezados en FastAPI . 😎

##  Modelo de respuesta - Tipo de retorno

Puede declarar el tipo utilizado para la respuesta anotando el tipo de retorno de la función de operación de ruta .
Puede utilizar anotaciones de tipo de la misma manera que lo haría para los datos de entrada en los parámetros de función , puede utilizar modelos de Pydantic, listas, diccionarios, valores escalares como números enteros, booleanos, etc.

#### response_model:



- response_model Parámetro
Hay algunos casos en los que necesitas o deseas devolver algunos datos que no son exactamente los que declara el tipo.

- response_model Prioridad¶
Si declara tanto un tipo de retorno como un response_model, response_modeltendrán prioridad y serán utilizados por FastAPI.

- Utilice el parámetro del decorador de operaciones de rutaresponse_model para definir modelos de respuesta y, especialmente, para garantizar que se filtren los datos privados.
Úselo response_model_exclude_unsetpara devolver solo los valores establecidos explícitamente.

##### 📤 Modelo de Respuesta (Response Model)
El modelo de respuesta es el "escudo" de tu API. Controla qué datos salen hacia el cliente.
Puntos Clave:
- Filtrado Automático: Si un campo no está en el modelo de respuesta, no se envía (ideal para ocultar passwords o IDs internos).
- Conversión de Tipos: Si devuelves un objeto de base de datos (ORM), FastAPI lo convierte automáticamente a JSON basándose en el modelo.
- Seguridad: Evita la fuga de información sensible accidental.
- Pro-Tip: Siempre intenta que tus modelos de entrada (UserCreate) sean diferentes a tus modelos de salida (UserOut). Esto te da un control total sobre el ciclo de vida del dato.

#### Eplicaion del ejemplo en "06_coffee_shop_integrator.py"

🧠 Arquitectura de la Solución
- Modelos de Datos (Pydantic): Definen la forma de la información. Field valida el contenido.
- Tipos Reutilizables (Annotated): Son "super-tipos" que empaquetan la validación. Ayudan a que el código sea DRY (Don't Repeat Yourself).
- Operaciones de Ruta: Son los verbos de tu aplicación (POST = Crear, GET = Leer).
- Response Model: Es el contrato final. Garantiza que el cliente reciba exactamente lo que prometimos y nada más.