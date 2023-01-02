# import Statements

from fastapi import APIRouter
from models.student import Student
from config.database import connection

# schemas
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

# endPoints
student_router = APIRouter()

# get all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

# Get one Studendet with matching ID
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    # Find a student and delete it and also returns the same student object
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


# Create a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

# Update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    connection.local.student.find_one_and_update(
        # Buscar el Id
        {"_id": ObjectId(studentId)},
        # Setear nuevos valores, Object itself 
        {"$set": dict(student)}    
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# Delete a student
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    # Find a student and delete it and also returns the same student object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))

@student_router.get('/test')
async def test():
    return "mensaje de prueba"

