from pydantic import BaseModel

_blacklist = []

def addToList(n):
    _blacklist.append(n)

class BlacklistPostBodyModel(BaseModel):
    number: int
