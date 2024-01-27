from fastapi import APIRouter

from app.models.fibonacci import main as fibonacciModel

router = APIRouter()

@router.get("/fibonacci/number")
def read_root():
    return fibonacciModel.getNNumbers(100, 0)


@router.get("/fibonacci/number/{index}")
def read_item(index: int):
    return {"status": "to be implemented"}