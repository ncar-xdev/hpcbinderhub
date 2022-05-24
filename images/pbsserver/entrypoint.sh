#!/bin/sh
hostname=$(hostname)
echo "Please set the PBS_SERVER environment variable:  export PBS_SERVER=$hostname"
sed -i "s/PBS_SERVER=.*/PBS_SERVER=$hostname/" /etc/pbs.conf
sed -i "s/PBS_START_SERVER=0/PBS_START_SERVER=1/" /etc/pbs.conf
sed -i "s/PBS_START_SCHED=0/PBS_START_SCHED=1/" /etc/pbs.conf
sed -i "s/PBS_START_COMM=0/PBS_START_COMM=1/" /etc/pbs.conf
sed -i "s/\$clienthost .*/\$clienthost $hostname/" /var/spool/pbs/mom_priv/config
/etc/init.d/pbs start
/opt/pbs/bin/qmgr -c "set server flatuid=true"
/opt/pbs/bin/qmgr -c "set server acl_roots+=alpha@*"
/opt/pbs/bin/qmgr -c "set server acl_roots+=beta@*"
/opt/pbs/bin/qmgr -c "set server operators+=alpha@*"
/opt/pbs/bin/qmgr -c "set server operators+=beta@*"
while [ $# -gt 0 ]
do
    /opt/pbs/bin/qmgr -c "create node $1"
    shift
done
exec sleep infinity
