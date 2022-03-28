# ZincBase

...

https://github.com/complexdb/zincbase


## Members

...

## Installation Guide

```
pip install zincbase
pip install zincbase[web]
pip install --upgrade python-socketio==4.6.0
pip install --upgrade python-engineio==3.13.2
pip install --upgrade Flask-SocketIO==4.3.1

sudo apt install redis-server
```

Or, instead, use ```pip install -r requirements.txt```.

## Run

Terminal 1: ```python -m zincbase.web --redis 127.0.0.1:6379```
Terminal 2: ```python countries.py```
