#!/usr/bin/env python3
"""
Usage: sudo python3 setup.py

TireFire installation script

Author: @nullidy
"""
import os
import subprocess
import sys
from shutil import which, copy
import pathlib

def main():
    display_setup()

def install():
    if not verify_tirefire_dir():
        exit()

    dependencies = get_system_dependencies()

    installed_dependencies = verify_installed_dependencies(dependencies)

    to_install = []

    for i in dependencies:
        if i not in installed_dependencies:
            to_install.append(i)
    install_system_dependencies(to_install)

    not_installed = verify_installed_dependencies(dependencies)
    if not_installed is not None:
        print("Not all dependencies installed")
        # log_error(f"The following were not installed {' '.join(not_installed)}")
    
    # install_python_dependencies()
    create_tirefire_dir()
    create_tirefire_links()

def display_setup():
    """Display TireFire install welcome banner
    """
    tirefire_banner = """
 _______  ___  ______    _______  _______  ___  ______    _______ 
|       ||   ||    _ |  |       ||       ||   ||    _ |  |       |
|_     _||   ||   | ||  |    ___||    ___||   ||   | ||  |    ___|
  |   |  |   ||   |_||_ |   |___ |   |___ |   ||   |_||_ |   |___ 
  |   |  |   ||    __  ||    ___||    ___||   ||    __  ||    ___|
  |   |  |   ||   |  | ||   |___ |   |    |   ||   |  | ||   |___ 
  |___|  |___||___|  |_||_______||___|    |___||___|  |_||_______|.py
"""
    print(tirefire_banner)
    print("Created by: @CoolHandSquid")

    if not get_response("Would you like to install TireFire? [yes/no] > "):
        print("Goodbye!")
        exit()
    
    install()

def verify_tirefire_dir() -> bool:
    """Verify current working directory is TireFire

    Returns:
        bool: true if in TireFire dir
    """
    current_dir = os.getcwd().split("/")[-1]
    if not current_dir == "TireFire":
        print("Installation of TireFire requires you be in the installation directory [TireFire]")
        return False
    else:
        return  True

def verify_installed_dependencies(dependencies: list) -> list:
    """get list of dependencies that are install on system

    Args:
        dependencies (list): list of tirefire required software

    Returns:
        list: [description]
    """
    installed_dependencies = []

    if dependencies is None:
        return []

    for i in dependencies:
        if which(i) is None:
            continue
        else:
            installed_dependencies.append(i)
    
    return installed_dependencies

def verify_wordlists():
    """check that required wordlists are on the system
    """
    pass

def install_system_dependencies(to_install: list):
    """install system packages with selected package manager

    Args:
        to_install (list): list of packages needing installed
    """
    if to_install is None:
        return

    install_message = f"The following packages need installed {', '.join(to_install)}\nWould you like to install them? [yes/no] > "
    
    if not get_response(install_message):
        print(f"You will need to manually install {', '.join(to_install)}")
        log_error(f"Error while installing dependencies... {', '.join(to_install)} are not installed")
        return

    package_managers = { 
        "apt": f"apt install {' '.join(to_install)} -y",
        "yay": f"yay -S {' '.join(to_install)}",
        "pacman": f"pacman -S {' '.join(to_install)}",
        "yum": f"yum install {' '.join(to_install)}",
        "dnf": f"dnf install {' '.join(to_install)}"
    }

    print("Which package manager would you like to use?")
    for k,v in enumerate(package_managers):
        print(f"{k+1}) {v}")
    package_manager = list(package_managers.keys())[int(input("> ")) - 1]

    print(package_managers[package_manager])
    subprocess.run(['sudo', package_managers[package_manager]])

def install_python_dependencies():
    """install python requirements.txt
    """
    if not get_response("Would you like to install python dependencies? [yes/no] > "):
        log_error("Python dependencies not installed\nRun: python3 -m pip install -r requirements.txt")
        return

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r','requirements.txt', '-y'])

def create_tirefire_links():
    home_dir = os.path.expanduser('~')
    if not get_response("Would you like to create symlink for /usr/bin/TireFire? [yes/no] > "):
        log_error("Symlink not created")
        return
    os.symlink(home_dir + "/.tirefire/TireFire.py", "/usr/bin/TireFire")
    print("Symlink created")

def create_tirefire_dir():
    """create tirefire directory in $HOME/.tirefire
    """
    home_dir = os.path.expanduser('~')
    print(f"Creating {home_dir}/.tirefire directory")
    pathlib.Path(home_dir + "/.tirefire").mkdir(parents=True, exist_ok=True) 
    print(f"Copying files to {home_dir}/.tirefire")

    files = os.listdir(".")

    for f in files:
        try:
            copy(f, home_dir + "/.tirefire")
        except FileNotFoundError as e:
            continue
    
    os.chdir(home_dir + "/.tirefire")
    os.mkdir("pictures")
    copy("Tire_Fire.jpg", "pictures")

def get_response(msg: str) -> bool:
    """get User response

    Args:
        msg (str): message to respond to

    Returns:
        bool: yes/no response
    """
    response = input(msg).lower()
    while True:
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("yes or no is required")
            continue

def get_wordlists():
    pass

def get_system_dependencies(software_file="software.txt") -> list:
    """Get list of dependencies to install

    Args:
        software (str, optional): path to software list. Defaults to "software.txt".

    Returns:
        list: list of software
    """
    software = []

    try:
        with open(software_file, "r") as f:
            for i in f:
                software.append(i.strip())
    except FileNotFoundError as e:
        log_error("Error while getting system dependencies... software file doesnt exist" + e)

    return software

def get_git_dependencies():
    print("Donwloading dirsearch...")
    subprocess.run(["git", "clone", "https://github.com/maurosoria/dirsearch.git"])
    print("Downloading impacket...")
    subprocess.run(["git", "clone", "https://github.com/SecureAuthCorp/impacket.git"])

def dconf_load():
    subprocess.run(["dconf load /com/gexperts/Tilix/ < tilix.dconf"])

def log_error(error: str):
    """log errors during installation

    Args:
        error (str): error to log
    """
    with open("install_log.txt", "a+") as f:
        f.write(error)

if __name__ == "__main__":
    main()

