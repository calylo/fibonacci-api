from fastapi import APIRouter

router = APIRouter()

@router.get("/fibonacci/number")
def read_root():
    return {"status": "to be implemented"}


@router.get("/fibonacci/number/{index}")
def read_item(index: int):
    return {"status": "to be implemented"}