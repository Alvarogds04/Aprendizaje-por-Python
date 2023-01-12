from fastapi import FastAPI 

app = FastAPI()

#Lanzar el server uvicorn backend.fastapi.main:app --reload 
#URL local= 127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastAPI"


#127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url":"http://alvaro.com"}



