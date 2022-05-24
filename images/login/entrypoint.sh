#!/bin/sh
/bin/sh /etc/entrypoint.sh
exec "/usr/sbin/sshd -D"
