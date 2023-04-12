from fastapi import FastAPI


app = FastAPI()


students = {
    1 : {
    "name" : "John",
    "age": 28,
    "class":"Year 94"
    },
    2 : {
    "name" : "Smith",
    "age": 82,
    "class":"Year 70"
    },
}
@app.get("/")
def index():
    return{"name":"First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The id of the student you want to view",gt=0, lt=3)):
    return students[student_id]