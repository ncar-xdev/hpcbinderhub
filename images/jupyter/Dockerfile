FROM base as jupyter
RUN dnf install -y wget git
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/jupyter
RUN . /opt/jupyter/etc/profile.d/conda.sh && \
    conda activate && \
    conda install -y -c conda-forge jupyterhub jupyterlab dask_labextension nb_conda_kernels && \
    pip install batchspawner sudospawner wrapspawner git+https://github.com/NERSC/sshspawner && \
    conda clean -y --all

FROM base
COPY --from=jupyter --chown=admin:admin /opt/jupyter /opt/jupyter
