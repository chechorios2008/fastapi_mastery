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

### 🍪 Netx topic
Parámetros de las cookies