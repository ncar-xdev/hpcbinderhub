# Login Node

The **Login Node** image (i.e., image name `login`) is designed to be a simple CentOS
image running an SSH Server and having PBS client utilities installed (i.e., so that
jobs can be submitted to the PBS queue from the login node).

From within this directory, build this Docker image with the following:

```console
> docker build --tag login .
```

## Manual Cluster Creation

To demonstrate the launch of a two-node cluster of independent SSH-accessible
containers, do the following:

```console
> docker network create login-net
> docker run -d --network login-net --hostname node1 --name node1 login
> docker run -d --network login-net --hostname node2 --name node2 login
```

This will stand up two nodes, called `node1` and `node2`, that are each running
an SSH server. You can now log into the `node1` container from your host system:

```console
> docker exec -it node1 bash
/ #
```

and then ssh from `node1` to `node2`:

```console
/ # ssh alpha@node2
```

using the `alpha` user's password.

### Manual Teardown

To take down the manually created cluster, do the following:

```console
> docker stop node1 node2
> docker rm node1 node2
> docker network rm login-net
```

## Docker Compose Cluster Creation

A two-node cluster can be easily created with Docker Compose, as well.
From within this directory, run the following:

```console
> docker-compose up -d
```

and it will stand up two nodes, `node1` and `node2`, connected via a
network called `login-net`, just like in the manual example above.

### Docker-Compose Teardown

To take down the Docker Composed cluster, do the following:

```console
> docker-compose down
```
