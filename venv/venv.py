#!/bin/env python3

from subprocess import run as _run
from time import ctime as _ctime
from os import system as _sys
from os import getenvb as _getenv
from os.path import exists as _ispath
from os import mkdir as _mkdir
from os import listdir as _ls
from os import stat as _stat
from os import chdir as _chdir
from urllib.request import urlopen as _get
from sys import argv as _argv

BC = "https://raw.githubusercontent.com/Madhava-mng/bc/main/venv/lists"
#BC = "http://127.0.0.1:8000/lists"
R, G, N = "\u001b[31;1m", "\u001b[32;1m","\u001b[00m"
E = {
        "UTG": f"{R}[!] Please turn on your mobile data, unable to get data.{N}",
        "HFS": " S.NO      LINUX-ENV\n ----      ---------",
        "HFL": " S.NO       NAME         SIZE            CREATED\n ----       ----         ----            -------",
        "ENF": f"{R}[!] Environment not found.\n available env:{N}",
        "EAE": f"{R}[!] env already exist{N}.\nenter 'y' to over write it. {G}[y/n]{N}: ",
        "RMM": f"{R}[!] enter 'y' to remove permenently. {G}[y/n]{N}: ",
        "Y": ["y", 'yes', 'yep'],
        "RUN": "venv run <env>",
        "RME": "venv remove <env>",
        "PER": "venv pull <env> [name]",
        "HELP": """venv: linux vritual environment for termux. (v0.0.1)\n
    show            Print all linux environment.
    pull <name>     Pull linux environment.
    list            Print all pulled linux env.
    run <name>      Launch env.
    remove <name>   Remove the env permenently.
    help, --help    To show this message.

$ venv pull alpine test1
$ venv list
$ venv run
$ venv remove test1

source: Andronix  os: Android  written: Python3.x.x"""
        }
PARRENT_PATH = _getenv(b"HOME").decode()+"/.venv"



if(not _ispath(PARRENT_PATH)):
    _mkdir(PARRENT_PATH)


def show_env():
    count = 1
    try:
        DATA = eval(_get(BC).read())
        print(E["HFS"])
        for i in DATA.keys():
            print(f" [{count:0>2}]   {i:^15}")
            count += 1
    except:
        print(E["UTG"])

def list_():
    count = 1
    if (len(_ls(PARRENT_PATH)) > 0):
        print(E["HFL"])
        for i in _ls(PARRENT_PATH):
            s = _run(["du", "-sh", PARRENT_PATH+"/"+i], capture_output=True).stdout[:-1].split(b"\t")[0].decode()
            t = _ctime(_stat(PARRENT_PATH+"/"+i).st_atime)
            print(f" [{count:0>2}]  {i:^15}   {s}    {t}")
            count += 1


def pull(env, name=""):
    try:
        if(name == ""):
            name = env
        DATA = eval(_get(BC).read())
        if(env in DATA.keys()):
            if(not _ispath(PARRENT_PATH+"/"+name)):
                _mkdir(PARRENT_PATH+"/"+name)
            else:
                if(input(E["EAE"]).lower() not in E["Y"]):
                        return 0
            _chdir(PARRENT_PATH+"/"+name)
            _sys(DATA[env])
        else:
            print(E["ENF"], G,list(DATA.keys()), N)
    except:
        print(E["UTG"])

def remove(env_name):
    if(input(E["RMM"]).lower() in E["Y"]):
        _sys("rm -rf "+PARRENT_PATH+"/"+env_name+ " 2>/dev/null")
    else:
        print(E["RME"])

def run(env):
    if(_ispath(PARRENT_PATH+"/"+env)):
        _chdir(PARRENT_PATH+"/"+env)
        _sys("./star*.sh")
    else:
        print(E["RUN"])




for i in range(len(_argv)):
    if(_argv[i] in ("help", "--help", "h")):
        print(E['HELP'])
        raise SystemExit()
    if(_argv[i] in ("list", "l")):
        list_()
        raise SystemExit()
    if(_argv[i] in ("show", "s")):
        show_env()
        raise SystemExit()
    if(_argv[i] in ("run", "r")):
        try:
            run(_argv[i+1])
        except IndexError:
            print(E["RUN"])
        raise SystemExit()
    if(_argv[i] in ("remove", "rm")):
        try:
            remove(_argv[i+1])
        except IndexError:
            print(E["RME"])
        raise SystemExit()
    if(_argv[i] in ("pull", "p")):
        try:
            pull(_argv[i+1], _argv[i+2])
        except IndexError:
            try:
                pull(_argv[i+1])
            except IndexError:
                print(E["PER"])
        raise SystemExit()
