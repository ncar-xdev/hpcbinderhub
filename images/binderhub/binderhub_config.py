# flake8: noqa
from urllib.parse import urlparse

from binderhub.build_local import LocalRepo2dockerBuild

c.BinderHub.debug = True

c.BinderHub.auth_enabled = True
c.BinderHub.builder_required = False
c.BinderHub.build_class = LocalRepo2dockerBuild
c.BinderHub.push_secret = None
# c.BinderHub.hub_url = 'http://jupyterhub:8000'
# c.JupyterHub.hub_ip = 'http://jupyterhub'

c.BinderHub.about_message = "This is a local deployment without Kubernetes"
