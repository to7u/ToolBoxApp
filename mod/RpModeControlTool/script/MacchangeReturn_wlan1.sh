#!/bin/bash
macchanger -s wlan1
sudo ifconfig wlan1 down
sudo macchanger -p wlan1
macchanger -s wlan1
sudo ifconfig wlan1 up
