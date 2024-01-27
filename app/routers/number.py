from typing import Annotated
from fastapi import APIRouter, Query

from app.models.fibonacci import main as fibonacciModel

router = APIRouter()


@router.get("/number")
def read_root(
    page: Annotated[int | None, Query(title="page number to get", ge=0)] = 0,
    page_size: Annotated[int | None, Query(title="page number to get", ge=1)] = 100
):
    return fibonacciModel.get_page(page, page_size)


@router.get("/number/{index}")
def read_item(index: int):
    return fibonacciModel.get_number(index)
