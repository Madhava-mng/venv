# venv
vritual invironment for termux

## installation:
* copy the command and past it in to termux

```bash
#copy from hear
pkg update && pkg upgrade -y &&\
pkg install wget python -y &&\
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
```

## show all env:
```bash
$ venv show
```

## pull env:
* pull [distro] [name]
* [name] is optional
```bash                    
$ venv pull alpine test1
```

## list pulled env:
```bash
$ venv list
```

## launch:
* run [name]
```bash
$ venv run test1
```

## remove:
* remove [name]
```bash
$ venv remove test1
```

## source:
* Andronix
## os:
* Android
## language:
* Python3.x.x

## uninstall:
```bash
$ apt remove venv
```
