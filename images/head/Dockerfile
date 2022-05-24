FROM base
RUN dnf install -y openssh-server openssh-clients && \
    dnf clean all
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin no/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config && \
    sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config && \
    sed -ie "s/# Host */Host */g" /etc/ssh/ssh_config && \
    sed -ie "s/#   StrictHostKeyChecking ask/  StrictHostKeyChecking accept-new/g" /etc/ssh/ssh_config && \
    ssh-keygen -A
EXPOSE 22/tcp
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/root/entrypoint.sh"]
