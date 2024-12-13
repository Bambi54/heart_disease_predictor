from pydantic import BaseModel


class PredictDTO(BaseModel):
    x: int