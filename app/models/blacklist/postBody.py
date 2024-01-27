from pydantic import BaseModel

class BlacklistPostBodyModel(BaseModel):
    number: int
