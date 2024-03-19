from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gradio as gr

from src.utils.logger import logger
from src.server.router import v1Router, clip
from src.utils.config import Config
from src.core.clip import ClipInference

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

        self.clip = clip

    def fast_api_serve(self) -> None:
        uvicorn.run(self.server, port=self.config.clip.server.port, host=self.config.clip.server.host)
    

    def gradio_server(self):
        im = gr.Image(type="pil", label="Input Image")
        text = gr.Textbox(lines=2, placeholder="Enter your text here...")
        demo = gr.Interface(
            fn=clip.infer,
            inputs=[im, text],
            outputs=[gr.Label()],
            # live=True,
        )
        try:
            demo.launch(server_port = self.config.clip.server.port)
        except KeyboardInterrupt:
            print("\n")
            logger.error("Keyboard Interrupted...")
            sys.exit(0)
