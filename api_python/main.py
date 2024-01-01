#FastAPI crea la API (GET,POST,PUT,DELETE)
#HTTPException genera excepciones
#Request envía una petición
#Body: genera cuerpo del json
#Path valida ruta
#Query valida parametros query
#Depends clase que indica que una clase que hereda depende de otra

from fastapi import Depends, FastAPI, HTTPException, Request, Body, Path, Query

#HTMLResponse  imprime HTML - JSONResponse imprime JSON
from fastapi.responses import HTMLResponse, JSONResponse

#BaseModel crea un esquema de datos #Field valida campos
from pydantic import BaseModel, Field

#Optional genera atributos opcionales en las clases. - List para obtener modelos de respuesta
from typing import Optional, List

#Importando token y validación
from jwt_manager import create_token, validate_token

#Importando middleware de autenticación
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "API"
app.version = "0.0.1"


#Creando esquema del middleware para validar token
class JWTBearer(HTTPBearer):
    #Deber ser una función asincrona ya que toma su tiempo
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(
                status_code=403,
                detail=
                f"Credenciales son inválidas, usuario ingresado: {data['email']}"
            )


#Creando un esquema de información del usuario
class User(BaseModel):
    email: str
    password: str


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


# Ruta de login
@app.post('/login', tags=['Auth'])
def login(user: User):
    #Simulando validación
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)


#Consulta todas las peliculas
#Agregando modelo de respuesta response_model
#Agregando códigos de estado status_code
#Agregando validación middleware Depends


@app.get('/movies',
         tags=['Movies'],
         response_model=List[Movie],
         status_code=200,
         dependencies=[Depends(JWTBearer())])
def get_movies() -> List[
    Movie]:  # -> List[Movie] indica que vamos a retornar una lista de peliculas
    return JSONResponse(status_code=200, content=movies)  #Retornando un JSON


#Consulta pelicula por id
@app.get('/movies/{id}',
         tags=["Movies"],
         response_model=Movie,
         status_code=200)
def get_movie_by_id(id: int = Path(ge=1, le=2000)) -> Movie:  #Path valida ruta
    #Filtrando
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=404, content=[])


#Parámetros query - Query valida parámetros query


@app.get('/movies/', tags=["Movies"], response_model=List[Movie])
def get_movies_by_query(category: str = Query(min_length=5, max_length=15),
                        year: int = Query(default=None, ge=1900,
                                          le=2024)) -> List[Movie]:
    if year is None:
        data = [movie for movie in movies if movie['category'] == category]
        return JSONResponse(content=data)
    else:
        data = [
            movie for movie in movies
            if movie['category'] == category and movie['year'] == year
        ]
        return JSONResponse(content=data)


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
@app.post('/movies/clase',
          tags=['Movies-Clase'],
          response_model=dict,
          status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201,
                        content={"message": "Se ha registrado la pelicula"})


# ******Método PUT*******


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


@app.put('/movies/clase/{id}', tags=['Movies-Clase'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            #item['id'] = id
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(
                content={"message": "Se ha modificado la pelicula"})


# ******Método DELETE*******


@app.delete('/movies/{id}',
            tags=['Movies'],
            response_model=dict,
            status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(
                status_code=200,
                content={"message": "Se ha eliminado la pelicula"})
