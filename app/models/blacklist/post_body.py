from pydantic import BaseModel, Field


class BlacklistPostBodyModel(BaseModel):
    number: int = Field(ge=0)
