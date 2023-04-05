#!/bin/bash
macchanger -s wlan1
sudo ifconfig wlan1 down
macchanger -r wlan1
macchanger -s wlan1
sudo ifconfig wlan1 up
