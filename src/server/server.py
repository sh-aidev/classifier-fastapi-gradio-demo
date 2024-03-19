from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gradio as gr
import sys
from src.utils.logger import logger
from src.server.router import v1Router, classifier
from src.utils.config import Config
from src.core.classifier import ClassifierInference

class APIServer:
    def __init__(self):
        root_config_dir = "configs"
        logger.debug(f"Root config dir: {root_config_dir}")

        self.config = Config(root_config_dir)
        logger.debug("Configs Loaded...")

        self.server = FastAPI()
        self.server.add_middleware(
            CORSMiddleware,
            allow_origins = ["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            
        )
        self.server.include_router(v1Router, prefix="/v1")

        self.classifier = classifier

    def fast_api_serve(self) -> None:
        uvicorn.run(self.server, port=self.config.classifier.server.port, host=self.config.classifier.server.host)
    

    def gradio_server(self):
        im = gr.Image(type="pil", label="Input Image")
        demo = gr.Interface(
            fn=self.classifier.infer,
            inputs=[im],
            outputs=[gr.Label(num_top_classes = 10)],
        )
        try:
            demo.launch(server_name = self.config.classifier.server.host, server_port = self.config.classifier.server.port)
        except KeyboardInterrupt:
            print("\n")
            logger.error("Keyboard Interrupted...")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(0)
