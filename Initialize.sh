#/bin/bash
export DISPLAY=:0
python3.13 ~/python-test/ShowMSG.py &

sleep(5)
python3.13 ~/python-test/Initialize.py
#/usr/local/bin/python3.13 ~/python-test/Handshke.py
