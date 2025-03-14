#!/usr/bin/env python3
import os
import pprint
import pwd
import argparse
import shlex
import subprocess
from netaddr import *

parser = argparse.ArgumentParser(
        description='TireFire is Powered by book.hacktricks.xyz.',
        epilog="TireFire -i tilix --update 10.169.254.56",)
parser.add_argument("IP", help="IP adress or hostname of the target", type=str)
parser.add_argument('-i', '--interaction_terminal', default='tmux', help='Interact with TireFire via "tmux" or "tilix". tmux is default')
parser.add_argument('-u', '--updatedb', action="store_true", help='Update to the latest TireFire database') 
try:
    args    = parser.parse_args()
except:
    print("example_syntax: {}".format(parser.epilog))
    exit()

cwd     = os.getcwd()
tfdir   = subprocess.getoutput("readlink /usr/local/bin/TireFire")
tfdir   = tfdir[:-11]

try:
    IP      = IPAddress(args.IP)
    hostname = args.IP.replace('.','_')
except:
    hostname = IP = args.IP

def init_updatedb():
    print("Updating database")
    subprocess.run(shlex.split("curl https://raw.githubusercontent.com/CoolHandSquid/TireFire/TireFire_V4/Main.csv --output {}/Main.csv".format(tfdir)), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Updating database complete")

def init_TireFire_tmux():
    hassession  = subprocess.run(shlex.split("tmux has-session -t TireFire_{}".format(hostname)), stderr=subprocess.DEVNULL)
    if hassession.returncode == 0:
        print("A session for {} already exists. Exiting".format(IP))
        exit()
    else:
        pass
    
    subprocess.run(shlex.split("tmux new-session -s TireFire_{} -n Main -c {} -d".format(hostname, cwd)))
    subprocess.run(shlex.split("tmux send-keys -t TireFire_{}:0.0 '{}TireFire_tmux.py {} {} {} {}' Enter".format(hostname, tfdir, IP, hostname, cwd, tfdir)))
    print("TireFire session for {} named TireFire_{} has started successfully!\nList of running Tmux sessions:".format(IP, hostname))
    subprocess.run(shlex.split("tmux ls"))
    print("\ncopy-paste (or hotkey w if already inside tmux):\ntmux a -t TireFire_{}".format(hostname))

def init_TireFire_tilix():
    if pwd.getpwuid(os.getuid())[0] != "root":
        print("Running the tilix inerface requres the user to be root.")
        exit()
    if os.environ['USER'] != "root":
        print("The shell environment user must be root. Try: sudo TireFire x.x.x.x -i tilix")
        exit()
    
    os.system("tilix --maximize -t 'TireFire  Main Page' -x $SHELL -c '{}TireFire_tilix.py {} ; $SHELL'".format(tfdir, IP))
    
if __name__ == "__main__":
    if args.updatedb == True:
        init_updatedb()
    if args.interaction_terminal == "tmux":
        init_TireFire_tmux()
    elif args.interaction_terminal == "tilix":
        init_TireFire_tilix()
    else:
        print("That interaction_terminal is not valid. Please chose tmux or tilix(ex: --interaction_terminal tilix).")
        exit()

