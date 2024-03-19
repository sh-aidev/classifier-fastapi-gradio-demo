import json, io
from typing import Annotated
from fastapi import APIRouter, File
from PIL import Image
from src.utils.config import Config
from src.core.clip import ClipInference

v1Router = APIRouter()
root_config_dir = "configs"
config = Config(root_config_dir)
clip = ClipInference(model_name = config.clip.clip_model.model_name, processor_name = config.clip.clip_model.processor_name)

@v1Router.post("/image-to-text", status_code=200)
def find_similarity(
    file: Annotated[bytes, File()],
    text: str
    ) -> dict:
    img = Image.open(io.BytesIO(file))
    img = img.convert("RGB")
    return clip.infer(img, text)

@v1Router.get("/health")
def health():
    return {"message": "ok"}