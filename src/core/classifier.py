import torch

from PIL import Image
from torchvision import transforms
import requests

from src.utils.logger import logger


class ClassifierInference:
    def __init__(self, model_name: str, model_path: str) -> None:
        self.model_name = model_name
        self.model_path = model_path
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        if model_path != "":
            self.model = torch.load(model_path)
        else:
            self.model = torch.hub.load('pytorch/vision:v0.6.0', model_name, pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        response = requests.get("https://git.io/JJkYN")
        self.labels = response.text.split("\n")

    def infer(self, img: Image) -> dict:
        img = self.transform(img)
        img = img.unsqueeze(0)
        with torch.no_grad():
            prediction = torch.nn.functional.softmax(self.model(img)[0], dim=0)
            confidences = {self.labels[i]: float(prediction[i]) for i in range(1000)}    

        return confidences