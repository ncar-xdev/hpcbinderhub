# SSH Server

This is an Alpine Linux-based Docker image that runs the SSHD service. It is set
up to disallow root login, and it creates an `admin` user with `sudo` permissions
that can log on via ssh to the running container.

From within this directory, build this Docker image with the following:

```console
> docker build --tag sshd .
```

## Manual Cluster Creation

To demonstrate the launch of a two-node cluster of independent SSH-accessible
containers, do the following:

```console
> docker network create ssh-net
> docker run -d --network ssh-net --hostname node1 --name node1 sshd
> docker run -d --network ssh-net --hostname node2 --name node2 sshd
```

This will stand up two nodes, called `node1` and `node2`, that are each running
an SSH server. You can now log into the `node1` container from your host system:

```console
> docker exec -it node1 sh
/ #
```

and then ssh from `node1` to `node2`:

```console
/ # ssh admin@node2
```

## Docker Compose Cluster Creation

A two-node cluster can be easily created with Docker Compose, as well.
From within this directory, run the following:

```console
> docker-compose up -d
```

and it will stand up two nodes, `node1` and `node2`, connected via a
network called `ssd-net`, just like in the manual example above.
