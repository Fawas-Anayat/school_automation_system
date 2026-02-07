from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
def login():
    return {
        "message" : "user logged in successfully"
    }