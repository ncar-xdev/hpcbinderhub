FROM centos:8.4.2105 AS builder
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget git
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/conda
COPY sshspawner /tmp/sshspawner
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate && \
    conda install -y nodejs && \
    conda install -y -c conda-forge jupyterhub jupyterlab dask_labextension nb_conda_kernels && \
    pip install jupyter-repo2docker repo2podman batchspawner sudospawner wrapspawner \
        git+https://github.com/jupyterhub/binderhub /tmp/sshspawner && \
    conda clean -y --all

FROM centos:8.4.2105
COPY --from=builder /opt/conda /opt/conda
