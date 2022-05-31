FROM base
RUN dnf install -y wget
RUN wget -qO /root/get_port.py https://raw.githubusercontent.com/NERSC/sshspawner/master/scripts/get_port.py

FROM client
RUN dnf install -y openssh-server && \
    dnf clean all
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin prohibit-password/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication yes/PasswordAuthentication yes/g" /etc/ssh/sshd_config && \
    sed -ie 's/#   Port 22/  Port 22/g' /etc/ssh/sshd_config
COPY --chown=jupyter:jupyter --from=getter /root/get_port.py /opt/conda/bin/get_port.py
COPY --chown=jupyter:jupyter --chmod=755 sshspawner-singleuser /opt/conda/bin/sshspawner-singleuser
CMD [ "/usr/sbin/sshd",  "-D" ]
