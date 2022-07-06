# Configuration file for jupyterhub.
# flake8: noqa
import os

import batchspawner
import sshspawner
import sudospawner
import wrapspawner

c.JupyterHub.allow_named_servers = True
c.JupyterHub.data_files_path = "/opt/conda/share/jupyterhub"
c.JupyterHub.spawner_class = "wrapspawner.ProfilesSpawner"
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_connect_ip = "jupyterhub.cluster.net"
c.ConfigurableHTTPProxy.api_url = "http://jupyterhub.cluster.net:5432"
c.Spawner.notebook_dir = "~/"

# ---------------------------------------------
# Register the BinderHub as an external service
# ---------------------------------------------
binder_client_id = os.getenv("BINDER_CLIENT_ID")
if not binder_client_id:
    raise ValueError("BINDER_CLIENT_ID not set")
binder_api_token = os.getenv("BINDER_API_TOKEN")
if not binder_api_token:
    raise ValueError("BINDER_API_TOKEN not set")

c.JupyterHub.services = [
    {
        "name": "binder",
        "oauth_client_id": binder_client_id,
        "api_token": binder_api_token,
        "oauth_redirect_uri": "http://localhost:8585/oauth_callback",
        "oauth_roles": ["user"],
    },
]
c.JupyterHub.load_roles = [
    {
        "name": "user",
        # grant all users access to all services
        "scopes": ["access:services", "self"],
    }
]

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
c.SSHSpawner.ssh_keyfile = "/etc/ssh/client"
c.SSHSpawner.hub_api_url = f"http://{c.JupyterHub.hub_connect_ip}:8081/hub/api"
c.SSHSpawner.path = (
    "/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/pbs/bin:/opt/conda/bin"
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
conda activate
{cmd}
"""
