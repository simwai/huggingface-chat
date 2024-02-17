# Execute streamlit run index.py in venv of .venv folder

import subprocess
import os
import sys


def is_running_in_venv() -> bool:
    if hasattr(sys, "real_prefix"):
        # This attribute is present in virtualenv environments
        return True
    elif sys.base_prefix != sys.prefix:
        # This condition is for venv environments in Python 3.3+
        return True
    else:
        return False


def run_streamlit():
    # Activate the virtual env for Unix-like systems
    activate_venv = None

    # Check if venv is already enabled
    if not is_running_in_venv():
        print("Not running inside a virtual environment")
        with open(activate_venv) as f:
            exec(f.read(), {"__file__": activate_venv})
        return

    print("Running inside a virtual environment")

    if os.name == "posix":
        activate_venv = os.path.join(".venv", "bin", "activate")
    elif os.name == "nt":
        activate_venv = os.path.join(".venv", "Scripts", "activate")

    subprocess.run(["streamlit", "run", "index.py"])


if __name__ == "__main__":
    run_streamlit()
