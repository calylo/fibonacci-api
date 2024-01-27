from typing import Annotated
from fastapi import APIRouter, Query

from app.models.fibonacci import main as fibonacciModel

router = APIRouter()

@router.get("/fibonacci/number")
def read_root(
    page: Annotated[int | None, Query(title="page number to get", ge=0)] = 0, 
    pageSize: Annotated[int | None, Query(title="page number to get", ge=1)] = 100
):
    return fibonacciModel.getPage(page, pageSize)


@router.get("/fibonacci/number/{index}")
def read_item(index: int):
    return fibonacciModel.getNumber(index)
