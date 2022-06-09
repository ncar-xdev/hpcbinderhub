# Configuration file for jupyterhub.
# flake8: noqa
import batchspawner
import sshspawner
import sudospawner
import wrapspawner

c.Application.log_level = 0
c.JupyterHub.allow_named_servers = True
c.JupyterHub.data_files_path = "/opt/jupyter/share/jupyterhub"
c.JupyterHub.spawner_class = "wrapspawner.ProfilesSpawner"
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_connect_ip = "jupyterhub.cluster.net"
c.ConfigurableHTTPProxy.api_url = "http://jupyterhub.cluster.net:5432"
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
c.SSHSpawner.remote_port_command = (
    "/opt/jupyter/bin/python /opt/jupyter/bin/get_port.py"
)
c.SSHSpawner.path = (
    "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/pbs/bin:/opt/jupyter/bin"
)

# --------------------------------
# BatchSpawner
# --------------------------------
c.TorqueSpawner.batch_query_cmd = "qstat -fx {job_id}"
c.TorqueSpawner.state_pending_re = r"job_state = [QH]"
c.TorqueSpawner.state_running_re = r"job_state = R"
c.TorqueSpawner.state_exechost_re = r"exec_host = ([\w_-]+)/"
c.TorqueSpawner.batch_script = """#!/bin/bash -l
#PBS -l walltime=00:05:00
#PBS -k eo
#PBS -N jupyter-singleuser
#PBS -V
env
conda activate
{cmd}
"""
