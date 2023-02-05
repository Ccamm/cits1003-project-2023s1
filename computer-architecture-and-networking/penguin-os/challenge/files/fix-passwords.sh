#!/bin/bash

while :;
do
    echo "" > /var/log/supervisor/fixpasswords.log;
    echo "[$(date)] Cleared /var/log/supervisor/fixpasswords.log to prevent passwords being stolen";
    echo "[$(date)] Reverting passwords to prevent other penguins from breaking things";
    echo "[$(date)] Setting USERNAME=penguinusr PASSWORD=UWA{fTpLipP3r5}";
    echo "penguinusr:UWA{fTpLipP3r5}" | chpasswd;
    echo "[$(date)] Setting USERNAME=alex PASSWORD=gonnawhackmykeyboardtomakesecure92p8yij37u49723ihuj23esdf";
    echo "alex:gonnawhackmykeyboardtomakesecure92p8yij37u49723ihuj23esdf" | chpasswd;
    sleep 60
done