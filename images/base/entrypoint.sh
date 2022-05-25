#!/bin/sh
sed -i "s/PBS_SERVER=.*/PBS_SERVER=$PBS_SERVER/" /etc/pbs.conf
exec $@
