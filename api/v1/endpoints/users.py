from fastapi import APIRouter

router = APIRouter()

@router.get("/welcone")
def get_user():
    return {
        "message" : "welcome to the fastapi"
    }

@router.post("/pics")
def load_user():
    return {
        "message" : "these are all the pics of the user"
    }