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
c.SSHSpawner.remote_port_command = "/opt/conda/bin/python /opt/conda/bin/get_port.py"
c.SSHSpawner.path = (
    "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/pbs/bin:/opt/conda/bin"
)

c.BatchSpawnerBase.req_runtime = "01:00:00"
c.BatchSpawnerBase.req_nprocs = "2"

# c.TorqueSpawner.batch_submit_cmd = "/opt/pbs/bin/qsub"
# c.TorqueSpawner.batch_query_cmd = "/opt/pbs/bin/qstat -x {job_id}"
# c.TorqueSpawner.batch_cancel_cmd = "/opt/pbs/bin/qdel {job_id}"
c.TorqueSpawner.batch_script = """#!/bin/sh
#PBS -l walltime={runtime}
#PBS -l nodes=1
#PBS -N jupyter-singleuser
{cmd}
"""

c.ProfilesSpawner.profiles = [
    (
        "Launch Locally",
        "local",
        "jupyterhub.spawner.LocalProcessSpawner",
        {"ip": "0.0.0.0"},
    ),
    ("Launch on HEAD Node", "head", "sshspawner.sshspawner.SSHSpawner", dict()),
    ("Launch in PBS Queue", "pbs", "batchspawner.TorqueSpawner", dict()),
]
