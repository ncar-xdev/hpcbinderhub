# flake8: noqa
from urllib.parse import urlparse

from binderhub.build_local import LocalRepo2dockerBuild

c.BinderHub.debug = True
c.BinderHub.builder_required = False
c.BinderHub.build_class = LocalRepo2dockerBuild
c.BinderHub.push_secret = None

c.BinderHub.about_message = "This is a local deployment without Kubernetes"

c.BinderHub.base_url = "/"
c.BinderHub.hub_url = "http://localhost:8000/"
c.BinderHub.hub_url_local = "http://jupyterhub:8000/"
c.BinderHub.hub_api_token = "dummy-binder-secret-token"

c.BinderHub.auth_enabled = True
url = urlparse(c.BinderHub.hub_url)
c.HubOAuth.hub_host = f"{url.scheme}://{url.netloc}"
c.HubOAuth.api_token = c.BinderHub.hub_api_token
c.HubOAuth.api_url = c.BinderHub.hub_url + "/hub/api/"
c.HubOAuth.base_url = c.BinderHub.base_url
c.HubOAuth.hub_prefix = c.BinderHub.base_url + "hub/"
c.HubOAuth.oauth_redirect_uri = "http://localhost:8585/oauth_callback"
c.HubOAuth.oauth_client_id = "binder-oauth-client-test"
