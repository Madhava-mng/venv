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
from socket import socket as _socket
from os import get_terminal_size as _size
from json import loads as _loads

BC = "https://raw.githubusercontent.com/Madhava-mng/bc/main/venv/lists"
VERSION = '0.0.4'



#BC = "http://127.0.0.1:8000/lists"
R, G, N, B, Y = "\u001b[31;1m", "\u001b[32;1m","\u001b[00m", "\u001b[34;1m", "\u001b[33;1m"
E = {
        "UTG": "[!] Please turn on your mobile data, unable to connect.",
        "HFS": " S.NO      LINUX-ENV\n ----      ---------",
        "HFL": " S.NO       NAME         SIZE            CREATED\n ----       ----         ----            -------",
        "ENF": f"{R}[!] Environment not found.\n{N} available env: ",
        "EAE": f"[!] env already exist{N}.\nenter 'y' to over write it. {G}[y/n]{N}: ",
        "RMM": f"{R}[!] enter 'y' to remove permenently. {G}[y/n]{N}: ",
        "Y": ["y", 'yes', 'yep'],
        "RUN": """
venv run <arg> <name>
     -t, --torify  Connect whole env to tor for anonymity.
        """,
        "RME": "venv remove <env>",
        "PER": "venv pull <env> [name]",
        "HELP": f"""venv: linux viritual environment for termux. (v{VERSION})\n
    show            Print all linux environment
    pull <name>     Pull linux environment.
    list            Print all pulled linux env.
    run <name>      Launch env. arg: [--tor, -t, --torify]
    remove <name>   Remove the env permenently.
    upgrade         Check for update.
    kill-tor, kill  kill tor service.
    help, --help    To show this message.


$ venv show
$ venv pull alpine test1      # set the name to test1
$ venv list
$ venv run test1
$ venv run --torify test1     # connect env to tor
$ venv remove test1

source: Andronix  os: Android  written: Python3.9"""
        }

PARRENT_PATH = _getenv(b"HOME").decode()+"/.venv"

#  proxychains configaration

PROXY_CONF = """
static_chain
remote_dns_subnet 224
proxy_dns
tcp_read_time_out 8000
tcp_connect_time_out 8000
[ProxyList]
socks4  127.0.0.1 9050
"""

# update and install proxychains

UPDATE_INSTALL = """
apt update -y 2>/dev/null
apt upgrade -y 2>/dev/null
apt install proxychains4 -y 2>/dev/null
pacman -Syu --noconfirm 2>/dev/null
pacman -S --noconfirm proxychains 2>/dev/null
apk update 2>/dev/null
apk upgrade 2>/dev/null
apk add proxychains-ng 2>/dev/null
dnf install fedora-upgrade 2>/dev/null
fedora-upgrade 2>/dev/null
dnf install proxychains 2>/dev/null
xbps-install -Su 2>/dev/null
xbps-install proxychains 2>/dev/null
zypper update 2>/dev/null
zypper dup 2>/dev/null
if [ -f /usr/bin/proxychains ];then rm /root/setup.sh;fi
"""



if(not _ispath(PARRENT_PATH)):
    _mkdir(PARRENT_PATH)

def note(text, c):
    print(c+text+('.'*(_size()[0]-len(text)-1)), N)

def check_for_packages(name):
    if _ispath('/data/data/com.termux/files/usr/bin/'+name):
        note('[+] Package '+name+' found', G)
    else:
        note('[!] Package '+name+' Not found', R)
        note('[+] Installing', G)
        _sys('pkg install -y tor')




def update():
    try:
        DATA = _loads(_get("https://raw.githubusercontent.com/Madhava-mng/venv/main/venv/manifest.json").read())['version']
        if(DATA != VERSION):
            note('[!] Update available venv(v'+DATA+")", R)
            if(input(G+'[?] Do you want to upgrade now. '+Y+'[Y/n]: ').lower() not in ['n', 'no']):
                note('[+] Upgrading to (v'+DATA+')', G)
                dir_ = _run(["mktemp", '-d'], capture_output=True).stdout.decode()
                note('[+] Temp: '+dir_[:-1], G)
                _sys("cd "+dir_+"\nwget https://github.com/Madhava-mng/venv/raw/main/venv/venv_"+DATA+"_all.deb.tar && tar -xvf venv_"+DATA+"_all.deb.tar && apt install ./venv_"+DATA+"_all.deb")
        else:
            note('[+] Package uptodate (v'+VERSION+")", B)
    except:
        note(E['UTG'], R)
        raise SystemExit()


def tor(source):
    service = _socket()
    tmp = ""
    note('[!] Check for tor package', B)
    check_for_packages('tor')
    note('[?] Check for Tor service status', Y)
    update()
    try:
        service.connect(('127.0.0.1', 9050))
        service.close()
        note('[*] Tor service is already running', B)
    except:
        note('[+] Starting Tor service', G)
        _sys('tor 1>/dev/null 2>/dev/null&')

    note('[+] Connected to Tor', G)

    # copy the file as source

    _sys('cp start*.sh .source')

    # rewtite the file

    with open(".source", "r") as file_buffer:
        for i in file_buffer.readlines():
            if(i[-9:-1] == '--login"'):
                tmp += i[:11]+'proxychains -q -f /root/.proxy.conf '+i[11:]
            else:
                tmp += i
    file_buffer.close()
    with open(".source",  "w") as file_buffer:
        file_buffer.write(tmp)
    file_buffer.close()
    _sys('./.source')


def show_env():
    count = 1
    try:
        DATA = eval(_get(BC).read())
        print(E["HFS"])
        for i in DATA.keys():
            print(f" [{count:0>2}]   {i:^15}")
            count += 1
    except:
        note(E["UTG"], R)


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
    env = env.strip()
    try:
        if(name == ""):
            name = env
        DATA = eval(_get(BC).read())
        note("[+] Pulling "+env+" as "+name, G)
        if(env in DATA.keys()):
            if(not _ispath(PARRENT_PATH+"/"+name)):
                _mkdir(PARRENT_PATH+"/"+name)
            else:
                if(input(E["EAE"]).lower() not in E["Y"]):
                        return 0
            _chdir(PARRENT_PATH+"/"+name)
            _sys(DATA[env])
            _sys("echo '"+UPDATE_INSTALL+"' > "+PARRENT_PATH+"/"+name+"/"+env+"-fs/root/setup.sh")
            _sys("echo '"+PROXY_CONF+"' > "+PARRENT_PATH+"/"+name+"/"+env+"-fs/root/.proxy.conf")
            note("[*] Run 'venv run "+name+"'to launch env", B)
            note("[#] run 'sh setup.sh' inside venv for undate and tor conectivity", G)
        else:
            print(E["ENF"], G,list(DATA.keys()), N)
    except:
        print(E["UTG"])

def remove(env_name):
    if(input(E["RMM"]).lower() in E["Y"]):
        _sys("rm -rf "+PARRENT_PATH+"/"+env_name+ " 2>/dev/null")
    else:
        print(E["RME"])

def run(env, TOR=False):
    if(_ispath(PARRENT_PATH+"/"+env)):
        _chdir(PARRENT_PATH+"/"+env)
        source = './start-*.sh'
        if(TOR):
            tor(source)
        else:
            _sys(source)
    else:
        print(E["RUN"])


if(len(_argv) > 1):
    if(_argv[1] in ['l', 'list']):
        list_()
    elif(_argv[1] in ['kill', 'kill-tor']):
        _sys('killall tor 2>/dev/null')
    elif(_argv[1] in ['u', 'update', 'upgrade']):
        update()
    elif(_argv[1] in ['s', 'show', 'showall']):
        show_env()
    elif(_argv[1] in ['rm', 'remove', 'rmv']):
        if(len(_argv) > 2):
            remove(_argv[2])
        else:
            print(E['RME'])
    elif(_argv[1] in ['p', 'pull']):
        if(len(_argv) > 3):
            pull(_argv[2], _argv[3])
        elif(len(_argv) > 2):
            pull(_argv[2])
        else:
            print(E['PER'])
    elif(_argv[1] in ['r', 'run']):
        if(len(_argv) > 3):
            if(_argv[2] in "--tor -t --torify".split()):
                run(_argv[3], True)
            else:
                print(E['RUN'])
        elif(len(_argv) > 2):
            run(_argv[2])
        else:
            print(E['RUN'])
    else:
        print(E['HELP'])
else:
    print(E['HELP'])
