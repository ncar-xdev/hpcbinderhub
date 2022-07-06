FROM userbase
RUN mkdir -p /opt/conda/var/binderhub
COPY run_binderhub /opt/conda/bin/run_binderhub
COPY binderhub_config.py /opt/conda/etc/binderhub_config.py
EXPOSE 8585/tcp
CMD [ "/bin/bash", "/opt/conda/bin/run_binderhub" ]
