# BinderHub on HPC Demonstration

The `docker-compose.yml` file in the this directory contains the necessary
configuration for Docker Compose to launch a "fake" HPC cluster with Docker
Compose.

## How to Launch the Demonstration

To launch this demonstration, run Docker Compose from within this directory with:

```bash
$ docker-compose up -d
```

## How to Use the Demonstration

Once the demonstration cluster has been launched with Docker Compose (see previous
step), you can interact with the demonstration on your local machine. You can
see the JupyterHub by pointing your browser to `http://localhost:8000`. You can
see the BinderHub by pointing your browser to `http://localhost:8585`.

### Authentication

The first thing you will see on either the JupyterHub or the BinderHub is the
_authentication_ screen. This demonstration cluster has three "fake" users:
`alpha`, `beta`, and `gamma`. Their passwords are the same as their usernames.

This authentication page is provided by the JupyterHub service. So, even if you
visit the BinderHub, the page on which you are authenticating is being serviced
by the JupyterHub.

### The JupyterHub

Once you have authenticated on the JupyterHub, you will be presented with a
drop-down menu of options for spawning a single-user JupyterLab instance. This
option is being provided by the `ProfilesSpawner` that ships with
[`WrapSpawner`](https://github.com/jupyterhub/wrapspawner). It is not exactly
the same as what most HPC cluster JupyterHubs would deploy, but it provides the
same kind of service: namely, an HTML form that launches the appropriate JupyterHub
`Spawner` given the options selected on the page.

This demonstration cluster has the following options:

- _Launch Locally_: This option lets you launch a single-user JupyterLab instance
  directly on the same "node" on which the JupyterHub is running. (In this case,
  it launches the JupyterLab process inside the `jupyterhub` container.)
- _Launch on HEAD Node_: This option lets you launch a single-user JupyterLab
  instance on the "head node," or "login node." This is done with an `SSHSpawner`.
  The code for which was originally written by folks at NERSC and can be found
  [here](https://github.com/NERSC/sshspawner). To make it work on this demonstration
  cluster, some modifications needed to be made, and so that source code is provided
  in this repository in the `images/conda/sshspawner` directory.
- _Launch in PBS Queue_: This option lets you launch a single-user JupyterLab
  instance on a "compute node" via PBS. This is done with `BatchSpawner`, which
  can be found [here](https://github.com/jupyterhub/batchspawner).

### The BinderHub

Once you have authenticated with the JupyterHub, you will be presented with the
same page that you can see on [MyBinder](https://mybinder.org). On this web form,
you can provide a link to a "Binderized" git repository. Once you enter the
necessary fields in the form and click the "Launch" button, it will start building
an image to host your git-hosted notebook using
[Repo2docker](https://github.com/jupyterhub/repo2docker).

Since Docker is usually not welcome on HPC systems, this demonstration builds the
image with [Podman](https://podman.io/), instead. Podman is an HPC-friendly
containerization engine that is compatible with Docker. While Repo2docker is still
used in this demonstration, it is used with the `--engine=podman` option, which switches
the Docker operations in Repo2docker to use the
[Repo2podman](https://github.com/manics/repo2podman) plugin.

When this demonstration is launched, it will also launch a Docker image registry
running in the same cluster. This image registry will store all built images.

**NOTE: Currently, the BinderHub in this demonstration will build the Podman image
using Repo2docker/Repo2podman. However, the image is not pushed to the registry.
Nor is the image launched in the JupyterHub. Ideas for how to implement these steps
are detailed in the [issues](https://github.com/ncar-xdev/hpcbinderhub/issues) in
this repository.**
