#!/bin/bash
macchanger -s wlan0
sudo ifconfig wlan0 down
macchanger -p wlan0
macchanger -s wlan0
sudo ifconfig wlan0 up
