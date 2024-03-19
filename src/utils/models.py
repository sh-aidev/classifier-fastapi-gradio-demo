from pydantic import BaseModel

class LoggerModel(BaseModel):
    environment: str


class ServerModel(BaseModel):
    host: str
    port: int

class CLIPModel(BaseModel):
    model_name: str
    processor_name: str

class Model(BaseModel):
    logger: LoggerModel
    server: ServerModel
    clip_model: CLIPModel
