FROM base
RUN dnf install -y git && \
    dnf clean all
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge jupyterhub jupyterlab dask_labextension nb_conda_kernels && \
    pip install batchspawner sudospawner wrapspawner git+https://github.com/NERSC/sshspawner && \
    conda clean -y --all && \
    mkdir -p /opt/conda/var/jupyterhub
COPY jupyterhub_config.py /opt/conda/etc/
COPY run_jupyterhub /opt/conda/bin/
EXPOSE 8000/tcp
EXPOSE 8081/tcp
CMD [ "/bin/bash", "/opt/conda/bin/run_jupyterhub" ]
