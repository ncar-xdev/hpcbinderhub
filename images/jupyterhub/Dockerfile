FROM userbase
USER admin
RUN mkdir -p /opt/jupyter/var/jupyterhub
COPY --chown=admin:admin jupyterhub_config.py /opt/jupyter/etc/
COPY --chown=admin:admin run_jupyterhub /opt/jupyter/bin/
COPY --chown=admin:admin --chmod=755 sudospawner-singleuser /opt/jupyter/bin/
USER root
COPY jupyterhub.sudoers /etc/sudoers.d/jupyterhub
EXPOSE 8000/tcp 8081/tcp
CMD [ "sudo", "-u", "admin", "/bin/bash", "/opt/jupyter/bin/run_jupyterhub" ]
