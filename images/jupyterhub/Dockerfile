FROM base
RUN dnf install -y git && \
    dnf clean all
COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
COPY jupyterhub.pam /etc/pam.d/jupyterhub
USER jupyter
COPY --chown=jupyter:jupyter environment.yml /tmp/
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge mamba && \
    mamba env update --file=/tmp/environment.yml && \
    mamba clean -y --all && \
    rm -rf /tmp/environment.yml && \
    mkdir -p /opt/conda/var/jupyterhub
COPY jupyterhub_config.py /opt/conda/etc/
COPY run_jupyterhub /opt/conda/bin/
EXPOSE 8000/tcp
EXPOSE 8081/tcp
CMD [ "/bin/bash", "/opt/conda/bin/run_jupyterhub" ]
