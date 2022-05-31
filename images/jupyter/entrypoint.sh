#!/bin/sh
if [ $# -gt 0 ]
then
    echo "Copying /opt/miniconda3 to $1..."
    cp -r /opt/miniconda3/* $1
    shift
    echo "done."
fi
exec $@
