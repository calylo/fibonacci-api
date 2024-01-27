from fastapi import APIRouter

router = APIRouter()

@router.get("/fibonacci/blacklist")
def read_root():
    return {"status": "to be implemented"}


@router.post("/fibonacci/blacklist")
def create_item():
    return {"status": "to be implemented"}