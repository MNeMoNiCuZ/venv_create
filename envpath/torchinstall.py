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

# Helper function to construct the correct wheel filename with Python version twice
def get_wheel_filename(package_name, version, python_version, cuda_version):
    # Python version appears twice in the filename as per your existing files
    return f"{package_name}-{version}+{cuda_version}-{python_version}-{python_version}-win_amd64.whl"

# Helper function to check if a wheel exists in the cache
def is_wheel_in_cache(package_name, version, python_version, cuda_version):
    wheel_filename = get_wheel_filename(package_name, version, python_version, cuda_version)
    wheel_path = os.path.join(CACHE_DIR, wheel_filename)
    print(f"Searching for a local cache of {package_name} at: {wheel_path}...")
    if os.path.exists(wheel_path):
        print(f"Found local cache for {package_name}.")
        return wheel_path
    else:
        print(f"Local cache of {package_name} not found.")
        return None

# Helper function to download a wheel if it's not already cached
def download_wheel(package_name, version, python_version, cuda_version):
    index_url = f"{BASE_URL}/{cuda_version}"
    wheel_filename = get_wheel_filename(package_name, version, python_version, cuda_version)
    wheel_path = os.path.join(CACHE_DIR, wheel_filename)

    print(f"Will download {package_name} from {index_url} to {wheel_path}...")

    pip_download_command = [
        sys.executable, "-m", "pip", "download", package_name,
        f"--index-url={index_url}",
        "--no-deps",  # We only want the specific package, not dependencies
        "--dest", CACHE_DIR  # Save the wheel to the cache directory
    ]

    result = subprocess.run(pip_download_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(f"Downloaded {package_name} to {wheel_path}")
    else:
        print(f"Failed to download {package_name}. Error: {result.stderr}")
        sys.exit(1)

# Check for all wheels first and print the status of each one
def check_all_wheels(python_version, cuda_version):
    packages = {
        "torch": "2.4.1",
        "torchvision": "0.19.1",
        "torchaudio": "2.4.1"
    }

    missing_packages = []

    for package, version in packages.items():
        wheel_path = is_wheel_in_cache(package, version, python_version, cuda_version)
        if wheel_path:
            # If wheel is found, no need to download
            continue
        else:
            # If not found, mark it for download
            missing_packages.append((package, version))

    return missing_packages

# First check all wheels
missing_packages = check_all_wheels(python_version, cuda_version)

# Then download any missing wheels
for package, version in missing_packages:
    download_wheel(package, version, python_version, cuda_version)

print("Downloads completed. Now proceed to install using the appropriate command (pip or uv pip).")
