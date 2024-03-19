<div align="center">

# Image Classifier-FastAPI-Gradio-Demo
[![python](https://img.shields.io/badge/-Python_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
![license](https://img.shields.io/badge/License-MIT-green?logo=mit&logoColor=white)

This is a simple example of how to use FastAPI and Gradio to create a web-based image classifier. The model used is a pre-trained ResNet18 model from PyTorch.
</div>

## 📌 Feature
- [x] FastAPI server implemented
- [x] Gradio UI implemented
- [x] ResNet18 model used
- [x] Dockerized
- [x] Moduler code
- [x] Easy to deploy in AWS ECS
- [x] Easy to Integrate other models

## 📁  Project Structure
The directory structure of new project looks like this:

```
├── configs
│   └── config.toml
├── flagged
├── images
├── logs
│   └── server.log
├── main.py
├── README.md
├── requirements.txt
└── src
    ├── app.py
    ├── core
    │   ├── classifier.py
    │   └── __init__.py
    ├── __init__.py
    ├── pylogger
    │   ├── __init__.py
    │   └── logger.py
    ├── server
    │   ├── __init__.py
    │   ├── router.py
    │   └── server.py
    └── utils
        ├── config.py
        ├── __init__.py
        ├── logger.py
        ├── models.py
        └── textformat.pya
```

## 🚀 Getting Started

### Step 1: Clone the repository
```bash
git clone https://github.com/sh-aidev/classifier-fastapi-gradio-demo.git
cd classifier-fastapi-gradio-demo
```

### Step 2: Open inside docker container in vscode

```bash
code .
```
**NOTE**: Once repo in opened in vscode, it will ask to open in container. Click on reopen in container. It will take some time to build the container.

### Step 3: Install the required dependencies

```bash
python3 -m pip install -r requirements.txt
```
### Step 4: Create a .env file in root directory and add the following

```bash
SERVER=fastapi # fastapi or gradio
```
### Step 5: Run the server

```bash
python3 main.py
```

### Run from postman

```bash
# http://<ip/localhost>:8000/classifier?text=an image of a dog, image of a cat

# and give multiform data as body and upload image and send post request.
```

## 📜  References
- [FastAPI](https://fastapi.tiangolo.com/)
- [Gradio](https://www.gradio.app/)
- [PyTorch](https://pytorch.org/)
- [Docker](https://www.docker.com/)
- [AWS ECS](https://aws.amazon.com/ecs/)
- [DockerHub](https://hub.docker.com/)
- [TorchHub](https://pytorch.org/hub/)