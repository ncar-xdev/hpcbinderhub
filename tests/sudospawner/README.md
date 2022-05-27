# Simple JupyterHub Test

This Docker Compose setup is designed to test the JupyterHub Docker image
on its own. To start the test, type:

```console
> docker-compose up -d
```

and it should launch the `jupyterhub` image with the ports `8000` and `8081`
opened to the host system. You can then go to `http://localhost:8000` in your
browser to test the JupyterHub.

With this setup, you should only be able to run a JupyterLab session _locally_
on the JupyterHub server itself.
