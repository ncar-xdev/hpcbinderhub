# Configuration file for jupyterhub.
# flake8: noqa
import batchspawner
import sshspawner
import wrapspawner

c.JupyterHub.allow_named_servers = True
c.JupyterHub.data_files_path = "/opt/conda/share/jupyterhub"
c.JupyterHub.spawner_class = "wrapspawner.ProfilesSpawner"

c.Spawner.notebook_dir = "~/"

c.SSHSpawner.remote_hosts = ["head"]
c.SSHSpawner.remote_port = "22"
c.SSHSpawner.ssh_command = "ssh"
c.SSHSpawner.path = (
    "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/pbs/bin:/opt/jupyterhub/bin"
)
c.SSHSpawner.remote_port_command = "/usr/bin/python3 /opt/jupyterhub/bin/get_port.py"

c.BatchSpawnerBase.req_runtime = "01:00:00"
c.BatchSpawnerBase.req_nprocs = "2"

c.TorqueSpawner.batch_script = """#!/bin/sh
#PBS -l walltime={runtime}
#PBS -l nodes=1
#PBS -N jupyter-singleuser
{cmd}
"""

c.ProfilesSpawner.profiles = [
    ("Launch on HEAD Node", "head", "sshspawner.sshspawner.SSHSpawner", dict()),
    ("Launch in PBS Queue", "pbs", "batchspawner.TorqueSpawner", dict()),
]
