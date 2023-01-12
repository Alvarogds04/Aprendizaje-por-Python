from fastapi import FastAPI 
from pydantic import BaseModel

#Lanzar el server: uvicorn backend.Fastapi.main:app --reload 
#URL local= 127.0.0.1:8000

app = FastAPI()

# Entidad de user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
            User(id=2, name="Moure", surname="Dev",url="https://mouredev.com", age=35),
            User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]
            
@app.get("/usersjson")
async def usersjson():
    return [{"name":'Alvaro','surname':'Alexander','url' :"http://alvaro.com","age":35},
            {"name":'Moure','surname':'Dev','url' :"http://alvaro1.com","age":23},
            {"name":'Jose','surname':'Antena','url':"http://alvaro2.com","age":45}]


@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    user =filter(lambda user: user.id == id,users_list)
    try:
        return list(user)[0]
    except:
        return {'Error': 'no se ha encontrado el usuario'}


#QUERY 
@app.get("/user/")
async def user(id: int, name: str):
    return search_user(id)


#Introducir datos
@app.post ("/user/")
async def user (user: User):
    if type(search_user(user.id)) == User:
        return {'Error': 'El usuario ya existe'}
    else:
        users_list.append(user)


@app.put("/user/")
async def user(user:User):

    found =False

    for index,saved_user in users_list:
        if saved_user.id == user.id:
            users_list[index]= user
            found = True
        else:
            return {'Error': 'no se ha actualizado el usuario'}

#Buscar datos
def search_user(id: int):
    user =filter(lambda user: user.id == id,users_list)
    try:
        return list(user)[0]
    except:
        return {'Error': 'no se ha encontrado el usuario'}



