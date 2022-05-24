# Docker Images

The subdirectories contained in this directory define different Docker images
for use in this project. Each subdirectory contains a `Dockerfile` defining
how to build the image, and an `entrypoint.sh` file that defines what will be
done when the image is run.

## Base Image

All images a build on the `base` image, defined in the `base` directory. This
image, itself, is built on CentOS 8.4.2105. The base image installs `python3`,
the OpenSSH client utilities, and the OpenPBS client utilities. Thus, all
images have the ability to SSH into another machine and to submit jobs to the
PBS queue.

In addition to that software, the `base` image also defines a common set to
non-root users for all images: `alpha` and `beta`. The passwords for these
two users are `funkya` and `funkyb`, respectively.

**ENTRYPOINT:** The default entrypoint to the image configures the PBS client
tools to point to PBS Server at the hostname set by the environment variable
`PBS_SERVER`.

## Head Image

The `head` image is designed to be a _head node_ for the cluster. In addition
to the `base` image contents, the `head` image also installs the OpenSSH
server, so that users on other nodes can SSH into any head node. (NOTE: Only
`head` nodes can be entered via SSH!)

**ENTRYPOINT:** The default entrypoint to the image calls the `base` image
entrypoint and then runs the SSH server.

## PBS Server Image

The `pbsserver` image has installed the OpenPBS server and configures it to allow
the default users (see above) to submit jobs to the PBS queue.

**ENTRYPOINT:** The default entrypoint to the image configures the PBS Server
so that the default users can submit jobs to the queue and then starts the
PBS Server. Unlike the other entrypoints, the PBS Server image's entrypoint
accepts additional arguments via command line. Each additiional argument to
the image's entrypoint should be the hostname of a PBS MOM container.

## PBS MOM Image

The `pbsmom` image has the OpenPBS MOM process installed, which allows the image's
corresponding containers to act as PBS execution nodes (i.e., _compute_ nodes).

**ENTRYPOINT:** The default entrypoint to the image calls the `base` image
entrypoint, configures the MOM service to point to the appropriate PBS Server,
and then runs PBS MOM service.

## JupyterHub Image

The `jupyterhub` image has JupyterHub installed on it as well as the appropriate
Spawners for use with the other images.

**ENTRYPOINT:** The default entrypoint to the image calls the `base` image
entrypoint and then runs the JupyterHub service.

**PORTS:** In order to test the JupyterHub service, the ports `8000` and `8081`
(the JupyterHub API port) are exposed to the host system. Therefore, if these
ports are mapped from the running container to the same ports on the host, you
can see the Hub running at `http://localhost:8000/` in your browser.
