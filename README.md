# Binder for HPC Clusters

This repository contains a demonstration of how one _might_ deploy a BinderHub
service in an HPC system, next to an existing JupyterHub service. This demonstration
assumes that the existing JupyterHub service does not need extensive modifications
to work with the BinderHub (though some minor modifications are required).

The motivation for this experiment is to see how well Binder can work in an HPC
environment (where Docker isn't allowed) with minimal changes.

## Approach

The approach to this demonstration is to mock a real HPC system with Docker containers.
Each Docker container runs a different service, which makes it possible to "fake" an
HPC cluster on a single machine. To launch the demonstration(s), all you need to do
is run `docker-compose up -d` from within the appropriate demonstration directory (after
having built all of the Docker images locally on your machine).

Due to the nature of Docker containers, though, this will naturally be different than
a _real_ HPC cluster. I have tried to minimalize the differences, though, while also
trying to avoid what I _hope_ are unnecessary complications.

## Docker Images

The `images` directory contains instructions and files for building the Docker images
that represent the basic services and computing platforms that constitute a base
HPC cluster:

- a _head_ node, into which users can SSH,
- a PBS server, to which PBS jobs can be submitted (using a PBS client) and from which
  PBS jobs can be launched on the compute nodes,
- PBS MOM servers, on which PBS jobs will be launched, representing the compute nodes
  in the "fake" Docker/HPC cluster,
- a JupyterHub server, on which users can launch single-user Jupyter Lab instances
  on the JupyterHub server itself (i.e., _local_), on the head node (i.e., via SSH),
  or on the PBS compute nodes (i.e., via a submitted PBS job), and
- a BinderHub server, from which _authenticated_ JupyterHub users can launch Binderized
  notebooks on the HPC cluster.

The `demonstrations` directory contains different Docker Compose examples of different
HPC cluster deployments. Running these Docker Compose examples requires that the
Docker images defined in the `images` directory have been built. To build the images,
run `make` in the `images` directory or see the (README)[demonstrations/README.md] in
that directory for more details.
