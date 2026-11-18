# Small Head or Big Model?

Few-Shot Surface Defect Detection with a Frozen Foundation Model vs Vision LLMs
A frozen DINOv2 backbone with small trainable heads, tested on two domains:
- Industrial: steel surface defects (NEU-DET, Severstal)
- Everyday: car body damage such as dents and scratches (CarDD)

Methods compared:
1. Linear probe
2. LoRA
3. A cross-attention bridge that I will design myself (learnable queries attending to features from several layers of the frozen model)
## Requirements
- Python 3.12.6
- GPU: NVIDIA GeForce RTX 4060

## Setup
1. Install the repo by cloning
2. Create and activate .venv (replace your path accordingly):
    ```powershell
    python -m venv path-to-project\.venv  
    path-to-project\.venv\Scripts\activate
    ```
    In some windows machines, powershell will block the script, then use:
    ```powershell
     (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& path-to-project\.venv\Scripts\Activate.ps1)
     ```
3. Install PyTorch and CUDA:
    ```powershell
    pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132
    ```

## Check the environment
- Test if installation works by running the command in your project folder:
    ```powershell 
    python check_env.py 
    ``` 
- You should expect output: 
    > PyTorch version: 2.15.0+cu132<br>
CUDA available: True<br>
CUDA version: 13.2<br>
GPU 0: NVIDIA GeForce RTX 4060 Laptop GPU
