from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
        "category": "Acción"
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