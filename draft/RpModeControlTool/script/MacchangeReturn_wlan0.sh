#!/bin/bash
macchanger -s wlan0
ifconfig wlan0 down
macchanger -p wlan0
macchanger -s wlan0
ifconfig wlan0 up
