#!/bin/sh
/bin/sh /etc/entrypoint.sh
exec "/bin/bash /opt/jupyterhub/bin/run_jupyterhub"
