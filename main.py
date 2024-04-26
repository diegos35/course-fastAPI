from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from typing import Optional


app =  FastAPI()
app.title = 'Mi aplication con FastAPI'
app.version = "0.0.1"


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2010",
        "rating": 7.8,
        "category": "Amor"
    },
    {
        "id": 3,
        "title": "Diego",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2010",
        "rating": 7.8,
        "category": "Miedo"
    }
]

@app.get("/", tags=['home'])
def message():
    return  HTMLResponse('ok')


@app.get("/movies",tags=['movies'])
def get_movies():
   return movies


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
     return [movie for movie in movies if movie["id"] == id]
    ##movie = next((movie for movie in movies if movie["id"] == id), [])
    ##return movie


@app.get('/movies/', tags=['movies'])
#def get_movies_by_category(category: str, year: Optinal[int] = None):
def get_movies_by_category(category: str, year: str | None = None):
    filtered_movies = [movie for movie in movies if movie['category']== category]
    return {'count': len(filtered_movies), 'results': filtered_movies}  


@app.post('/movies', tags=['movies'])
def create_movies(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating:float= Body(), category:str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies