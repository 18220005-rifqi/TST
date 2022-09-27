import json
from fastapi import APIRouter

app =APIRouter()



@app.get("/")
async def hello() -> dict:
    return{
        "message" : "Hello World"
    }

student_list = [
    { "NIM" : 18220005, "Nama": "Muhammad Rifqi Riansyah Matondang"},
    { "NIM" : 18220007, "Nama": "Joanna Margareth Nauli"},
    { "NIM" : 18220009, "Nama": "Fatih Darielma Gaizta"}, ]

@app.post("/student")
async def add_student(student: dict) -> dict:
    student_list.append(student)
    return {"message":"Success"}

@app.get("/student")
async def get_student() -> dict:
    return {"student": student_list}


#with open("mahasiswa.json","r") as read_file:
 #   data = json.load(read_file)
#app = FastAPI()
#@app.get('/menu/{item_id')
#async def read_menu(item_id: int):
 #   for menu_item in data["menu"]:
 #       if menu_item['id'] == item_id:
 #           return menu_item
 #   raise HTTPException(
 #       status_code=404, detail=f'Item not found'
 #   )