FROM centos:8.4.2105 AS builder
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget git
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/binder && \
    mkdir -p /opt/binder/var/binderhub
RUN . /opt/binder/etc/profile.d/conda.sh && \
    conda activate && \
    conda install nodejs && \
    pip install git+https://github.com/jupyterhub/binderhub jupyter-repo2docker repo2podman && \
    conda clean -y --all

FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y podman
COPY --from=builder /opt/binder /opt/binder
COPY run_binderhub /opt/binder/bin/run_binderhub
COPY binderhub_config.py /opt/binder/etc/binderhub_config.py
EXPOSE 8585/tcp
CMD [ "/bin/bash", "/opt/binder/bin/run_binderhub" ]
