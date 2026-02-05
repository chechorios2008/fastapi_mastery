import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# 1. Obtenemos la ruta del directorio donde está este archivo main.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Unimos esa ruta con la carpeta 'templates'
template_path = os.path.join(base_dir, "templates")

# 3. Se lo pasamos a Jinja2
templates = Jinja2Templates(directory=template_path)

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/", include_in_schema=False, name="home")
# Route Aliasing (Alias de rutas)
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"},
        )


@app.get("/api/posts")
def get_posts():
    return posts

'''
include_in_schema=False: Esta es una joya de FastAPI. Al ponerlo en False, estas rutas no aparecerán
en la documentación de Swagger (/docs).
'''