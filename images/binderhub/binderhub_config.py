# flake8: noqa
from urllib.parse import urlparse

from binderhub.build_local import LocalRepo2dockerBuild
from binderhub.registry import DockerRegistry
from repo2podman.podman import PodmanEngine


class LocalRepo2podmanBuild(LocalRepo2dockerBuild):
    def get_r2d_cmd_options(self):
        """Get options/flags for repo2docker"""
        r2d_options = super().get_r2d_cmd_options()
        r2d_options.append("--engine=podman")
        r2d_options.append("--push")
        return r2d_options


c.BinderHub.debug = True

c.BinderHub.auth_enabled = True
c.BinderHub.builder_required = False
c.BinderHub.build_class = LocalRepo2podmanBuild

c.BinderHub.push_secret = None
c.BinderHub.use_registry = True
c.BinderHub.registry_class = DockerRegistry
c.DockerRegistry.url = "http://registry:5000/"
c.PodmanEngine.default_transport = "docker://registry:5000/"

c.BinderHub.about_message = "This is a local deployment without Kubernetes"
