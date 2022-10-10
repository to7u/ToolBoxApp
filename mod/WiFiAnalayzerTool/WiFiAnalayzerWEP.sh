#!/bin/sh

# Linux用shellscript 
# WEPのみ抽出
tput clear
while true; do
        nmcli -f IN-USE,SSID,BSSID,SIGNAL,SECURITY dev wifi | \
        egrep --color=always '^.*WEP.*$|$'
        tput ed
        sleep 1
        tput cup 0 0
done
