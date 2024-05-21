# Create Virtual Environment Scripts

This repository provides two batch scripts designed to simplify the creation and management of Python virtual environments on your system. With these scripts, you can quickly set up a new Python environment with just a few clicks, streamlining your development workflow.

## venv_create.bat

A comprehensive script that detects installed Python versions, allows custom naming of your virtual environment, offers an option to upgrade pip, and automatically places you inside the newly created environment.

### How to Use:
1. **Download and Place the Script**: Download `venv_create.bat` and place it in your desired directory.
2. **Run the Script**: Double-click the script to execute. It will display available Python versions for selection. The default selection is `1`.
3. **Name Your Environment**: Enter a name for your virtual environment when prompted. The default name is `venv`.
4. **Upgrade pip (Optional)**: Choose whether to upgrade pip. The default option is `Yes`.
5. **Install requirements.txt (Optional)**: Choose whether to run a `pip install -r requirements.txt` command in your new venv. The default option is `Yes`.
6. **Access Your Environment**: Upon completion, the script places you inside the virtual environment and creates an `activate_venv` script for re-entry in the future.

### Screenshots:

![venv_create.bat process](https://github.com/MNeMoNiCuZ/create_venv/assets/60541708/ee9212d5-6e27-4e0c-ac16-3ed4e2fd4481)

[![venv_create.bat completion](https://github.com/MNeMoNiCuZ/create_venv/assets/60541708/5ea123aa-b59f-4c99-8c98-c3d9aec3ac56)](https://github.com/MNeMoNiCuZ/create_venv/assets/60541708/5ea123aa-b59f-4c99-8c98-c3d9aec3ac56
)

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

---

By utilizing these scripts, developers can efficiently manage their Python environments, enhancing productivity and focusing more on development tasks.
