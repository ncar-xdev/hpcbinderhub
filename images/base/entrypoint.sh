#!/bin/sh
sed -i "s/PBS_SERVER=CHANGE/PBS_SERVER=${PBS_SERVER}/" /etc/pbs.conf
exec $@
