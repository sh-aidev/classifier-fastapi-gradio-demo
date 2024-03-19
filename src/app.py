import os
from src.server.server import APIServer


class App:

    def __init__(self) -> None:
        self.server = APIServer()

    def run(self):
        if os.getenv('SERVER', 'gradio') == "fastapi":
            self.server.fast_api_serve()
        else:
            self.server.gradio_server()