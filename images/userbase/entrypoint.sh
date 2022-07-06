#!/bin/sh
sed -i "s/PBS_SERVER=CHANGE/PBS_SERVER=${PBS_SERVER}/" /etc/pbs.conf
sysctl --system 1> /dev/null 2>&1
mount --make-rshared /
exec $@
