# Configuration file for jupyterhub.
# flake8: noqa
import batchspawner
import sshspawner
import sudospawner
import wrapspawner

c.JupyterHub.allow_named_servers = True
c.JupyterHub.data_files_path = "/opt/conda/share/jupyterhub"
c.JupyterHub.spawner_class = "wrapspawner.ProfilesSpawner"

c.Spawner.notebook_dir = "~/"

# --------------------------------
# WrapSpawner Profiles/Options
# --------------------------------
c.ProfilesSpawner.profiles = [
    ("Launch Locally", "local", "sudospawner.SudoSpawner", {}),
    ("Launch on HEAD Node", "head", "sshspawner.sshspawner.SSHSpawner", {}),
    ("Launch in PBS Queue", "pbs", "batchspawner.TorqueSpawner", {}),
]

# --------------------------------
# SSHSpawner
# --------------------------------
c.SSHSpawner.remote_hosts = ["head"]
c.SSHSpawner.remote_port_command = "/opt/conda/bin/python /opt/conda/bin/get_port.py"
c.SSHSpawner.path = (
    "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/pbs/bin:/opt/conda/bin"
)

# --------------------------------
# BatchSpawner
# --------------------------------
c.BatchSpawnerBase.req_runtime = "01:00:00"
c.BatchSpawnerBase.req_nprocs = "1"

# c.TorqueSpawner.batch_submit_cmd = "/opt/pbs/bin/qsub"
# c.TorqueSpawner.batch_query_cmd = "/opt/pbs/bin/qstat -x {job_id}"
# c.TorqueSpawner.batch_cancel_cmd = "/opt/pbs/bin/qdel {job_id}"
c.TorqueSpawner.batch_script = """#!/bin/sh
#PBS -l walltime={runtime}
#PBS -l nodes=1
#PBS -k eo
#PBS -N jupyter-singleuser
conda activate
{cmd}
"""
