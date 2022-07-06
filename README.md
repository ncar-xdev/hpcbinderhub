# Binder for HPC Clusters

An experiment in deploying Binder on HPC systems where Docker isn't allowed.

The `images` directory contains instructions and files for building Docker images that
represent the basic services and computing platforms that constitute a base
HPC cluster:

- a _head_ node, into which users can SSH,
- a PBS server, from which PBS jobs can be launched on the compute nodes,
- PBS MOM servers, which form the compute nodes in the Docker cluster,
- a JupyterHub server, on which users can launch single-user Jupyter Lab instances
  on the JupyterHub server itself (i.e., _local_), on the head node (i.e., via SSH),
  or on the PBS compute nodes (i.e., via a PBS job), and
- a BinderHub server, from which _authenticated_ users can launch Binderized
  notebooks on the HPC cluster.

The `examples` directory contains different Docker Compose examples of different
HPC cluster deployments. Running these Docker Compose examples requires that the
Docker images defined in the `images` directory have been built. To build the images,
run `make` in the `images` directory.
