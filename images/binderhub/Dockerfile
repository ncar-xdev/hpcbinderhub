FROM userbase
RUN mkdir -p /opt/jupyter/var/binderhub
COPY run_binderhub /opt/jupyter/bin/run_binderhub
COPY binderhub_config.py /opt/jupyter/etc/binderhub_config.py
EXPOSE 8585/tcp
CMD [ "/bin/bash", "/opt/jupyter/bin/run_binderhub" ]
