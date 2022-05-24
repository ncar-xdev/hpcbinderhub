#!/bin/sh
if [[ -z $PBS_SERVER ]]
then
    echo "ERROR: Hostname of PBS Server is needed to launch container"
    echo "       Please set the PBS_SERVER environment variable appropriately."
    exit 1
else
    sed -i "s/PBS_SERVER=.*/PBS_SERVER=$PBS_SERVER/" /etc/pbs.conf
fi
