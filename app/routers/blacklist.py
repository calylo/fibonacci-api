from typing import Annotated
from fastapi import APIRouter, Query

from app.models.blacklist import postBody, main as blacklistModel

router = APIRouter()

@router.get("/fibonacci/blacklist")
def read_root(
    page: Annotated[int | None, Query(title="page number to get", ge=0)] = 0, 
    pageSize: Annotated[int | None, Query(title="page number to get", ge=1)] = 100
):
    return blacklistModel.getPage(page, pageSize)


@router.post("/fibonacci/blacklist")
def create_item(item: postBody.BlacklistPostBodyModel):
    return blacklistModel.addToList(item.number)
