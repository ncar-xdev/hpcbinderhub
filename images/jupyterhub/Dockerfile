# Originally taken from the "monolithic" JupyterHub Docker file
# developed by Jared Baker (jbaksta) @ NCAR.  See the repo:
#
#     https://github.com/NCAR/hpc_jupyterhub_dev
#
# Modified to be non-monolithic, however.

FROM centos:latest

# Deal with the fact that CentOS 8 is no longer supported
RUN sed -i -e "s|mirrorlist=|#mirrorlist=|g" /etc/yum.repos.d/CentOS-* && \
    sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-*

# Basic Updates & System Installs
RUN dnf -y makecache && \
    dnf -y install wget ncurses sudo nano which passwd openssh epel-release \
      git-all

# Create appropriate groups for JupyterHub
RUN groupadd -g 500 jupyter && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m jupyter && \
    usermod -aG wheel jupyter && \
    mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin

# Create three test users and set their passwords
RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -G jupyterhub alpha && \
    echo "alpha:funkyduck" | chpasswd && \
    useradd -u 1002 -G jupyterhub beta &&  \
    echo "beta:funkybird" | chpasswd && \
    useradd -u 1003 -G jupyterhub zeta && \
    echo "zeta:funkydonkey" | chpasswd ;

COPY jupyterhub.pam /etc/pam.d/jupyterhub

USER jupyter
RUN wget -O /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/jupyterhub && \
    mkdir -p /opt/jupyterhub/var/jupyterhub

RUN . /opt/jupyterhub/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge jupyterhub

# TODO: Generate SSL Certificates

COPY jupyterhub_config.py /opt/jupyterhub/etc/
COPY run_jupyterhub /opt/jupyterhub/bin/
# COPY sudospawner-singleuser /opt/jupyterhub/bin/

EXPOSE 8000/tcp
CMD ["/bin/bash","/opt/jupyterhub/bin/run_jupyterhub"]
