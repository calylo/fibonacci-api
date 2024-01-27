from fastapi import APIRouter

from app.models.fibonacci import main as fibonacciModel

router = APIRouter()

@router.get("/fibonacci/number")
def read_root(page: int | None = 0, pageSize: int | None = 100):
    return fibonacciModel.getPage(page, pageSize)


@router.get("/fibonacci/number/{index}")
def read_item(index: int):
    return {"status": "to be implemented"}