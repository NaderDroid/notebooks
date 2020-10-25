#! /bin/bash
for ip in `seq 1 254`; do
    for ip1 in `seq 1 254`; do
    	ping -c 1 $1.$ip.$ip1 | grep '64 bytes' | cut -d " " -f 4 | tr -d ":" &
    done
done
