FROM continuumio/miniconda3:latest
RUN apt-get update && apt-get install -y nano sudo && apt-get clean
RUN groupadd -g 500 jupyter && \
    useradd -g 500 -u 500 -G shadow -m jupyter && \
    usermod -aG sudo jupyter && \
    mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub
RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -g 990 alpha && \
    echo "alpha:funkyduck" | chpasswd && \
    useradd -u 1002 -g 990 beta && \
    echo "beta:funkybird" | chpasswd
COPY jupyterhub.pam /etc/pam.d/jupyterhub
USER jupyter
RUN conda init && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda create -y -c conda-forge --prefix /opt/jupyterhub jupyterhub && \
    mkdir -p /opt/jupyterhub/var/jupyterhub
COPY jupyterhub_config.py /opt/jupyterhub/etc/
COPY run_jupyterhub /opt/jupyterhub/bin/
EXPOSE 8000/tcp
EXPOSE 8081/tcp
CMD ["/bin/bash","-l","/opt/jupyterhub/bin/run_jupyterhub"]
