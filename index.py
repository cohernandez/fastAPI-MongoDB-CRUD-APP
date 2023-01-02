# Import Statements
from fastapi import  FastAPI

# incluir rutas
from routes.student import student_router

# crear APP
app = FastAPI()

# register your routers
app.include_router(student_router)
