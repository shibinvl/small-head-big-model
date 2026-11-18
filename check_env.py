import torch

cuda_ok = torch.cuda.is_available()

print("PyTorch version:", torch.__version__)
print("CUDA available:", cuda_ok)
print("CUDA version:", torch.version.cuda)

if cuda_ok:
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No GPU available. Check the NVIDIA driver and the PyTorch install command.")