#!/bin/bash

#Backup Data from control.brandsonroad.com
cd ~
ls -lthr
mongodump --forceTableScan --db led --gzip --archive=mongoBackup_$(date +"%Y-%m-%d.gz")
ls -lthr