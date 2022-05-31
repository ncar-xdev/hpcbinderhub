# This image installs the base Jupyter software stack into /opt/conda

FROM centos:8.4.2105 as conda
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget git
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/conda
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate && \
    conda install -y -c conda-forge jupyterhub jupyterlab dask_labextension nb_conda_kernels && \
    pip install batchspawner sudospawner wrapspawner git+https://github.com/NERSC/sshspawner && \
    conda clean -y --all
