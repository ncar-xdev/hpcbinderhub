# Docker Images

The subdirectories contained in this directory define different Docker images
for use in this project. Each subdirectory contains a `Dockerfile` defining
how to build the image, as well as any additional files needed for the image
during build time.

All images are based on the CentOS 8.4.2105 image.

## Conda Image

The `conda` image builds and installs [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
In the base Conda environment, the main Jupyter-based software is installed.
This software is installed in the `/opt/conda` directory, which is then copied
into the corresponding directory on each image where Jupyter-based software
needs to be run.

## PBSRPMS Image

The `pbsrpms` image builds the OpenPBS RPMs for installation in the necessary
PBS images: `userbase`, `pbsmom` and `pbsserver`. The OpenPBS client, MOM, and
server RPMs are each built for installation in their necessary image.

## PBS Server Image

The `pbsserver` image installs the OpenPBS server RPM from the `pbsrpms` image
and sets up the server to run in the local network.

## User Base Image

The `userbase` image contains all of the client and user-facing software. It copies
over the `/opt/conda` software from the `conda` image, as well as the OpenPBS Client RPM
from the `pbsrpms` image, from which the OpenPBS Client is installed. It installs
the OpenSSH Client, as well. In addition to installing this software, it sets it up
so that it can be used from within the container. This image also creates and defines
permissions for all _users_ on the JupyterHub and BinderHub systems.

## PBS MOM Image

This image installs the OpenPBS MOM server RPM for the "compute nodes" from the
`pbsrpms` image. Since user code is expected to run on the compute nodes, this
image is built from the `userbase` image. Containers running this image can be
used to model "compute nodes" on the HPC cluster.

## Head Image

The `head` image installs and configures the OpenSSH server so that all users defined
in the `userbase` image can SSH into the node with their password. Hence, this
image is built from teh `userbase` image.

## JupyterHub Image

The `jupyterhub` image installs and configures the JupyterHub service to run as
the `admin` user. This image is built from the `userbase` image.

_NOTE: Since the users defined in the `userbase` image are also installed in this
image, the JupyterHub authentication is handled with the default PAM Authentication
method._

## BinderHub Image

The `binderhub` image installs and configures the BinderHub to use the JupyterHub
service provided by the `jupyterhub` image. It is built from the `userbase` image.
