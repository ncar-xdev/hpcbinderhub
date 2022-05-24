#!/bin/sh
hostname=$(hostname)
echo "Please set the PBS_SERVER environment variable:  export PBS_SERVER=$hostname"
sed -i "s/PBS_SERVER=.*/PBS_SERVER=$hostname/" /etc/pbs.conf
sed -i "s/PBS_START_SERVER=0/PBS_START_SERVER=1/" /etc/pbs.conf
sed -i "s/PBS_START_SCHED=0/PBS_START_SCHED=1/" /etc/pbs.conf
sed -i "s/PBS_START_COMM=0/PBS_START_COMM=1/" /etc/pbs.conf
sed -i "s/\$clienthost .*/\$clienthost $hostname/" /var/spool/pbs/mom_priv/config
/etc/init.d/pbs start
exec "/bin/bash"
