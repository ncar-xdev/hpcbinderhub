# Basic Dockerfile for building a monolithic JupyterHub

FROM centos:latest
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf -y makecache && \
    dnf -y install wget ncurses sudo which nano passwd openssh epel-release && \
    dnf clean all
RUN groupadd -g 500 jupyter && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m jupyter && \
    mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin
RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -G jupyterhub alpha && \
    echo "alpha:funkyduck" | chpasswd && \
    useradd -u 1002 -G jupyterhub beta &&  \
    echo "beta:funkybird" | chpasswd
COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
COPY jupyterhub.pam /etc/pam.d/jupyterhub
USER jupyter
RUN wget -O /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/jupyterhub && \
    mkdir -p /opt/jupyterhub/var/jupyterhub
RUN . /opt/jupyterhub/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge jupyterhub && \
    conda clean --all
COPY jupyterhub_config.py /opt/jupyterhub/etc/
COPY run_jupyterhub /opt/jupyterhub/bin/
EXPOSE 8000/tcp
EXPOSE 8081/tcp
ENTRYPOINT ["/bin/bash", "/opt/jupyterhub/bin/run_jupyterhub"]
