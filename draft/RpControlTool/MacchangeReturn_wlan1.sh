#!/bin/bash
macchanger -s wlan1
ifconfig wlan1 down
macchanger -p wlan1
macchanger -s wlan1
ifconfig wlan1 up
