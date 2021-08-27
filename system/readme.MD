### gunicorn/daphne
#### 1. move socket/service to Ubuntu
```shell
sudo cp *.service etc/systemd/system/
sudo cp *.socket etc/systemd/system
```
#### 2. build services
```shell
sudo systemctl start daphne.socket
sudo systemctl enable daphne.socket
```
#### 3. status/log
```shell
sudo systemctl status daphne
sudo journalctl -u daphne.socket
```
#### 注意:
* ExecStart需就主機daphne/gunicorn進行調整
```shell
which daphne
```