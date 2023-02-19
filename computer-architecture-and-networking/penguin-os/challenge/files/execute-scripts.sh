#!/bin/bash

while :;
do
    for f in /opt/admin-scripts/*;
    do
    if [ -x $f ]
    then
        echo "[$(date)] Executing $f";
        timeout 10 /usr/bin/bash "$f" > /opt/admin-scripts-output/$(basename "$f").output
    fi
    /usr/bin/rm -rf $f;
    done
    sleep 30;
    rm -rf /opt/admin-scripts-output/*
    sleep 30;
done