import json, io
from typing import Annotated
from fastapi import APIRouter, File
from PIL import Image
from src.utils.config import Config
from src.core.classifier import ClassifierInference

v1Router = APIRouter()
root_config_dir = "configs"
config = Config(root_config_dir)
classifier = ClassifierInference(model_name = config.classifier.classifier_model.model_name, model_path = config.classifier.classifier_model.model_path)

@v1Router.post("/classifier", status_code=200)
def find_similarity(
    file: Annotated[bytes, File()]
    ) -> dict:
    img = Image.open(io.BytesIO(file))
    img = img.convert("RGB")
    return classifier.infer(img)

@v1Router.get("/health")
def health():
    return {"message": "ok"}