#/bin/bash
export DISPLAY=:0
pkill -9 -f "$1"

python3.13 ~/python-test/ShowMSG.py &
python3.13 "$2" "$3" "$4" "$5" "$6" "$7"
#/usr/local/bin/python3.13 ~/python-test/Handshke.py
