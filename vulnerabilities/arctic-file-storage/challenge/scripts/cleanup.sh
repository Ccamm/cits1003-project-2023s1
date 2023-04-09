#!/bin/sh

while :;
do
    echo "[$(date)] Cleaning up files;"
    sqlite3 /directus/database/database.sqlite 'DELETE FROM directus_files;'
    rm -f /directus/uploads/*;
    sleep 180;
done