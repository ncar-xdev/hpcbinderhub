#!/bin/sh
hostname=$(hostname)
sed -i "s/PBS_SERVER=CHANGE/PBS_SERVER=${hostname}/" /etc/pbs.conf
sed -i "s/\$clienthost .*/\$clienthost $hostname/" /var/spool/pbs/mom_priv/config
/etc/init.d/pbs start
exec sleep infinity
