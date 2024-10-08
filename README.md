# Create Virtual Environment Scripts

This repository provides two batch scripts designed to simplify the creation and management of Python virtual environments on your system. With these scripts, you can quickly set up a new Python environment with just a few clicks, streamlining your development workflow.

## venv_create.bat

A script that detects installed Python versions, allows custom naming of your virtual environment, offers an option to upgrade pip, and automatically places you inside the newly created environment.

### How to Use:
1. **Download and Place the Script**: Download `venv_create.bat` and place it in your desired directory.
2. **Run the Script**: Double-click the script to execute. It will display available Python versions for selection. The default selection is `1`.
3. **Name Your Environment**: Enter a name for your virtual environment when prompted. The default name is `venv`.
4. **Upgrade pip (Optional)**: Choose whether to upgrade pip. The default option is `Yes`.
5. **Install requirements.txt (Optional)**: Choose whether to run a `pip install -r requirements.txt` command in your new venv. The default option is `Yes`.
6. **Access Your Environment**: Upon completion, the script places you inside the virtual environment and creates an `activate_venv` script for re-entry in the future.

### Screenshot:
![image](https://github.com/user-attachments/assets/b1a525b7-6f24-4cc8-8338-4d0c8597e0ab)

### Video Demonstration of setting up a venv
https://github.com/user-attachments/assets/5622e4c3-9782-49e3-bede-df558e2eda23


## venv_create_simple.bat

A streamlined version of the script for quick setup, skipping Python version selection and focusing on creating a virtual environment directly.

### How to Use:
1. **Download and Place the Script**: Obtain `venv_create_simple.bat` and place it in the target directory.
2. **Run the Script**: Execute the script. You will be prompted to name your virtual environment, with a default option provided.
3. **Access Your Environment**: The script will finalize the environment creation and provide an `activate_venv` script for easy access in the future.

#### Customizing Python Version:
To specify a Python version, edit line 10 of `venv_create_simple.bat` with your desired version.

### Screenshot:

![venv_create_simple.bat usage](https://github.com/MNeMoNiCuZ/create_venv/assets/60541708/952617c8-2579-4d61-a8c3-cec205c5c4ee)


## envpath folder
In this folder there are a few .bat-files.

The idea is to make these accessible to any CLI window, so that you can more quickly and easily install requirements.txt and pytorch from a cached location.

### How to setup (Windows)
1. **Open Environment Variables**: Open your start menu and type `environment variables`. Select the `Edit the system environment variables` shortcut`
2. **Environment Variables**: Click on the `Environment Variables`-button at the bottom right corner of the window.
3. **System variables > Path**: In the bottom half of the screen (System variables), scroll down the list until you see a `Path` entry. Select this and press the `Edit...`-button.
4. **Add new environment variable**: Press the New-button at the top right corner to add a new path variable.
5. **Enter the path to the envpath folder**: Paste the path to the /envpath/-folder from this github project on your local drive and press OK on all windows to save

Example setup of environment
![image](https://github.com/user-attachments/assets/17030b8f-03ec-476b-bc2f-6cbed6f07475)


### How to use
Any time you want to install a requirements.txt-file, all you can instead run one of the .bat-scripts for this.

* Type `req` to run the command: `pip install -r requirements.txt`

* Type `uvreq` to do the same as **req** but install it with `uv`, which installs it faster.

* Type `torch` to run the `torchinstall.py` script, which will check which version of CUDA you have installed, and then install pytorch with CUDA support. It caches the pytorch and reuses the cache for fast installations in the future.

* Type `uvtorch` to do the same as **torch** but install it with `uv`, which installs it faster.

### Video demonstration of installing pytorch

https://github.com/user-attachments/assets/500bc3be-f160-4ba1-a3d1-798f56114930


---

By utilizing these scripts, developers can efficiently manage their Python environments, enhancing productivity and focusing more on development tasks.
