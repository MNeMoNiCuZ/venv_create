import os
import sys
import subprocess

# Base URL for downloading wheels
BASE_URL = "https://download.pytorch.org/whl"
CACHE_DIR = os.path.expanduser("~/my-pip-cache").replace("/", "\\")

# Ensure cache directory exists
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Detect Python version in the format cp310, cp311, etc.
python_version = f"cp{sys.version_info.major}{sys.version_info.minor}"

# Detect CUDA version using nvcc command
def detect_cuda_version():
    try:
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            output = result.stdout
            for line in output.splitlines():
                if "release" in line:
                    version_str = line.split("release")[-1].split(",")[0].strip()
                    return f"cu{version_str.replace('.', '')}"  # Convert to format like cu118, cu121, etc.
    except Exception as e:
        print(f"Failed to detect CUDA version. Error: {e}")
    return None

# Get the latest CUDA version dynamically
cuda_version = detect_cuda_version()

if not cuda_version:
    print("CUDA version detection failed. Please ensure 'nvcc' is in your PATH.")
    sys.exit(1)

print(f"Detected Python version: {python_version}")
print(f"Detected CUDA version: {cuda_version}")

# Helper function to check if a wheel is cached
def is_wheel_cached(package_name):
    wheel_files = os.listdir(CACHE_DIR)
    for wheel_file in wheel_files:
        if package_name in wheel_file:
            print(f"Found cached version of {package_name} at {os.path.join(CACHE_DIR, wheel_file)}.")
            return os.path.join(CACHE_DIR, wheel_file)
    print(f"No cached version of {package_name} found.")
    return None

# Helper function to install package, uses cache if available
def install_package(package_name):
    if is_wheel_cached(package_name):
        print(f"Installing {package_name} from cache...")
    else:
        print(f"Downloading and installing the latest version of {package_name}...")
        pip_install_command = [
            sys.executable, "-m", "pip", "install", package_name,
            f"--index-url={BASE_URL}/{cuda_version}"
        ]
        result = subprocess.run(pip_install_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Successfully installed {package_name}.")
        else:
            print(f"Failed to install {package_name}. Error: {result.stderr}")
            sys.exit(1)

# Install the required packages (torch, torchvision, torchaudio)
for package in ["torch", "torchvision", "torchaudio"]:
    install_package(package)

print("Installation completed successfully!")
