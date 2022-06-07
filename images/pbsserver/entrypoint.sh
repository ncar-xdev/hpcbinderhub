#!/bin/sh
hostname=$(hostname)
sed -i "s/PBS_SERVER=CHANGE/PBS_SERVER=$hostname/" /etc/pbs.conf
sed -i "s/\$clienthost .*/\$clienthost $hostname/" /var/spool/pbs/mom_priv/config
/etc/init.d/pbs start
/opt/pbs/bin/qmgr -c "set server flatuid=true"
/opt/pbs/bin/qmgr -c "set server job_history_enable=1"
/opt/pbs/bin/qmgr -c "set server acl_roots+=alpha@*"
/opt/pbs/bin/qmgr -c "set server acl_roots+=beta@*"
/opt/pbs/bin/qmgr -c "set server acl_roots+=gamma@*"
/opt/pbs/bin/qmgr -c "set server operators+=alpha@*"
/opt/pbs/bin/qmgr -c "set server operators+=beta@*"
/opt/pbs/bin/qmgr -c "set server operators+=gamma@*"
while [ $# -gt 0 ]
do
    /opt/pbs/bin/qmgr -c "create node $1"
    shift
done
exec sleep infinity
