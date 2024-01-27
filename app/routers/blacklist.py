from typing import Annotated
from fastapi import APIRouter, Query

from app.models.blacklist import post_body, main as blacklistModel

router = APIRouter()


@router.get("/blacklist")
def read_root(
    page: Annotated[int | None, Query(title="page number to get", ge=0)] = 0,
    page_size: Annotated[int | None, Query(title="page number to get", ge=1)] = 100
):
    return blacklistModel.get_page(page, page_size)


@router.post("/blacklist")
def create_item(item: post_body.BlacklistPostBodyModel):
    return blacklistModel.add_to_list(item.number)
