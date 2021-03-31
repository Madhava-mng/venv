# venv
vritual invironment for termux

## installation:
* copy the command and past it in to termux

```bash
# copy from hear
pkg update &&\
pkg install wget &&\
wget https://github.com/Madhava-mng/venv/raw/main/venv/venv_0.0.1_all.deb.tar &&\
tar -xvf venv_0.0.1_all.deb.tar && apt install ./venv_0.0.1_all.deb
# ends hear
```



## usage:
```bash
$ venv --help
venv: linux vritual environment for termux. (v0.0.1)

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

source: Andronix  os: Android  written: Python3.x.x
```

## uninstall:
```bash
$ apt remove venv
```
