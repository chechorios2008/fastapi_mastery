from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Blog Engine Pro")

# 1. Etiquetas con enumeración.
class Tags(Enum):
    posts = "Publicaciones del Blog"
    users = "Gestión de usuarios"
    stats = "Estadisticas y reportes"

class Post(BaseModel):
    title: str
    content: str

# 2. Aplicaciones de configuración de ruta. 
@app.post(
    "/posts/",
    response_model=Post,
    status_code=status.HTTP_201_CREATED,
    # Configuraciones de documenetación
    tags=[Tags.posts],
    summary="Crear una nueva publicación",
    description="""
    Crea un post en el blog. 
    * Valida que el título no esté duplicado.
    * Notifica automáticamente a los suscriptores.
    * Soporta **Markdown** en el contenido.
    """,
    response_description="Publicación creada exitosamente"
)
async def create_post(post: Post):
    return Post


@app.get(
    "/stats/",
    tags=[Tags.stats],
    summary="Obtener metricas",
    deprecated=True
)
async def get_metrics():
    return {"views": 1500, "likes": 300}