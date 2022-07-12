FROM userbase
USER admin
RUN mkdir -p /opt/conda/var/jupyterhub
COPY --chown=admin:admin jupyterhub_config.py /opt/conda/etc/
COPY --chown=admin:admin run_jupyterhub /opt/conda/bin/
COPY --chown=admin:admin --chmod=755 sudospawner-singleuser /opt/conda/bin/
USER root
COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
EXPOSE 8000/tcp
CMD [ "sudo", "-E", "-u", "admin", "/bin/bash", "/opt/conda/bin/run_jupyterhub" ]
