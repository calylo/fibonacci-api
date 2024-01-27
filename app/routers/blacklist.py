from fastapi import APIRouter

from app.models.blacklist import postBody, main as blacklistModel

router = APIRouter()

@router.get("/fibonacci/blacklist")
def read_root():
    return {"status": "to be implemented"}


@router.post("/fibonacci/blacklist")
def create_item(item: postBody.BlacklistPostBodyModel):
    blacklistModel.addToList(item.number)
    return {"result": item.number}
