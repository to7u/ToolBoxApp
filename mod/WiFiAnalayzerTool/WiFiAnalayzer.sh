#!/bin/sh

# Linux用shellscript
tput clear #画面クリア
while true; do
        date +'%F %T'
        nmcli dev wifi
        tput ed #画面末までクリア
        sleep 1
        tput cup 0 0 #カーソルを0,0に移動
done
