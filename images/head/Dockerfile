FROM userbase
RUN dnf install -y openssh-server && \
    dnf clean all
RUN echo "TrustedUserCAKeys /etc/ssh/certauth.pub" >> /etc/ssh/sshd_config && \
    cp /root/keys/certauth.pub /etc/ssh/ && \
    echo "AuthorizedPrincipalsFile /etc/ssh/auth_principals/%u" >> /etc/ssh/sshd_config && \
    mkdir -p /etc/ssh/auth_principals && \
    echo -e "jupyter" > /etc/ssh/auth_principals/alpha && \
    echo -e "jupyter" > /etc/ssh/auth_principals/beta && \
    echo -e "jupyter" > /etc/ssh/auth_principals/gamma
COPY --chown=admin:admin get_port.py /opt/conda/bin/get_port.py
COPY --chown=admin:admin --chmod=755 sshspawner-singleuser /opt/conda/bin/sshspawner-singleuser
CMD [ "/usr/sbin/sshd",  "-D" ]
