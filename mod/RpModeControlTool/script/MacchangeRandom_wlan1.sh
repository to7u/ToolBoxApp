#!/bin/bash
macchanger -s wlan1
sudo ifconfig wlan1 down
sudo macchanger -r wlan1
macchanger -s wlan1
sudo ifconfig wlan1 up
