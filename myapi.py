from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1 : {
    "name" : "John",
    "age": 28,
    "year":"Year 94"
    },
    2 : {
    "name" : "Smith",
    "age": 82,
    "year":"Year 70"
    },
}


class Student(BaseModel):
    name:str
    age: int
    year:str

@app.get("/")
def index():
    return{"name":"First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The id of the student you want to view",gt=0)):
    return students[student_id]


@app.get("/get-by-name")
def get_student(*, name:Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}    


@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error":"Student exists"}
    
    students[student_id] = student
    return students[student_id]