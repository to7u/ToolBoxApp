#!/bin/bash
macchanger -s wlan0
ifconfig wlan0 down
macchanger -r wlan0
macchanger -s wlan0
ifconfig wlan0 up
