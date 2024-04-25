from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =  FastAPI()
app.title = 'Mi aplication con FastAPI'
app.version = "0.0.1"


@app.get("/", tags=['home'])
def message():
    return  HTMLResponse('ok')

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get("/movies",tags=['movies'])
def get_movies():
   return movies