from pydantic import BaseModel

class LoggerModel(BaseModel):
    environment: str


class ServerModel(BaseModel):
    host: str
    port: int

class ClasssifierModel(BaseModel):
    model_name: str
    model_path: str

class Model(BaseModel):
    logger: LoggerModel
    server: ServerModel
    classifier_model: ClasssifierModel
