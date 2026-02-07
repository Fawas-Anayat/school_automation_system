from api.v1.endpoints import users , auth
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router , prefix="/users" , tags=["users"])
app.include_router(auth.router, prefix="/login",tags=["login"])
