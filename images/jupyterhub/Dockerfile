# This image expects a volume attached at /opt/jupyter

FROM base AS jupyter
RUN dnf install -y wget git
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/miniconda3
RUN . /opt/miniconda3/etc/profile.d/conda.sh && \
    conda activate && \
    conda install -y -c conda-forge jupyterhub jupyterlab dask_labextension nb_conda_kernels && \
    pip install batchspawner sudospawner wrapspawner git+https://github.com/NERSC/sshspawner && \
    conda clean -y --all

FROM base
USER admin
COPY --from=jupyter --chown=admin:admin /opt/miniconda3 /opt/miniconda3
RUN mkdir -p /opt/miniconda3/var/jupyterhub
COPY --chown=admin:admin jupyterhub_config.py /opt/miniconda3/etc/
COPY --chown=admin:admin run_jupyterhub /opt/miniconda3/bin/
USER root
COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
EXPOSE 8000/tcp 8081/tcp
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/root/entrypoint.sh" ]
CMD [ "sudo", "-u", "admin", "/bin/bash", "/opt/jupyter/bin/run_jupyterhub" ]
