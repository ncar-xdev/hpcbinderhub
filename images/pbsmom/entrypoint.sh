#!/bin/sh
/bin/sh /etc/entrypoint.sh
hostname=$(hostname)
sed -i "s/PBS_SERVER=.*/PBS_SERVER=$PBS_SERVER/" /etc/pbs.conf
sed -i "s/PBS_START_MOM=0/PBS_START_MOM=1/" /etc/pbs.conf
sed -i "s/\$clienthost .*/\$clienthost $hostname/" /var/spool/pbs/mom_priv/config
/etc/init.d/pbs start
exec sleep infinity
