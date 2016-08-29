#!/bin/sh
#Add timestamp
TS=$(date +"%F")

#Specify how the tar archive will be named
backup_naomi="homedir-$TS"

#Tar it
tar -zcvf "$backup_naomi.tar.gz" /home/niit