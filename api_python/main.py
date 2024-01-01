#Crea la API (GET,POST,PUT,DELETE) - Body: genera cuerpo del json - Path valida ruta

from fastapi import FastAPI, Body, Path
from fastapi.responses import HTMLResponse  #Imprime HTML
#BaseModel crea un esquema de datos #Field valida campos
from pydantic import BaseModel, Field
from typing import Optional  #Genera atributos opcionales en las clases.

app = FastAPI()
app.title = "API"
app.version = "0.0.1"

#Creando un esquema de datos


class Movie(BaseModel):  #Se define clase
    #Definiendo atributos
    #id: int | None = None,  #Esta sintaxis indica que son atributos opcionales
    id: Optional[
        int] = None,  #Sintaxis None indica que son atributos opcionales
    title: str = Field(min_length=5, max_length=15)  #Field valida campos
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str

    #Permite dejar datos de ejemplo (placeholder)
    model_config = {
        "json_schema_extra": {
            "examples": [{
                "id": 1,
                "title": "Camino final 2",
                "overview": "Pelicula de terror 2 basada en hechos reales",
                "year": 2022,
                "rating": 9.3,
                "category": "Terror"
            }]
        }
    }


movies = [{
    'id': 1,
    'title': 'Avatar',
    'overview':
    "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
    'year': 2008,
    'rating': 7.8,
    'category': 'Drama'
}, {
    'id': 2,
    'title': 'GoodFather',
    'overview':
    "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
    'year': 2009,
    'rating': 7.8,
    'category': 'Drama'
}]

#**********Método GET***********


# Creando primer endpoint
@app.get('/', tags=['Home'])  # Agregando ruta de inicio
def message():
    #return "¡Hello world!" # Retornando mensaje
    #return {"Hello": "world"} # Retornando diccionario
    return HTMLResponse('<h1>Hello world</h1>')  # Retornando html


#Consulta todas las peliculas
@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies


#Consulta pelicula por id
@app.get('/movies/{id}', tags=["Movies"])
def get_movie_by_id(id: int = Path(ge=1, le=2000)):  #Path valida ruta
    #Filtrando
    for item in movies:
        if item["id"] == id:
            return item
    return []


#Parámetros query


@app.get('/movies/', tags=["Movies"])
def get_movies_by_query(category: str, year: int = None):
    if year is None:
        return [movie for movie in movies if movie['category'] == category]
    else:
        return [
            movie for movie in movies if movie['category'] == category
            and movie['year'] == year  ##valid_query(year, category, movie)
        ]


# ******Método POST*******
# El Body() ayuda que no quede como un query si no como un objeto que contiene cada valor especificado


@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(),
                 title: str = Body(),
                 overview: str = Body(),
                 year: int = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    movies.append({
        "id": id,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies


#Aplicando POST con una clase
@app.post('/movies/clase', tags=['Movies-Clase'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies


# ******Método UPDATE*******


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int,
                 title: str = Body(),
                 overview: str = Body(),
                 year: int = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    for item in movies:
        if item["id"] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return movies


#Aplicando PUT con una clase


@app.put('/movies/clase/{id}', tags=['Movies-Clase'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['id'] = id
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies


# ******Método DELETE*******


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
