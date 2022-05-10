FROM alpine:latest
RUN apk --update add --no-cache openssh nano sudo
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin no/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config && \
    sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config && \
    sed -ie "s/# Host */Host */g" /etc/ssh/ssh_config && \
    sed -ie "s/#   StrictHostKeyChecking ask/  StrictHostKeyChecking accept-new/g" /etc/ssh/ssh_config && \
    ssh-keygen -A && \
    echo "" > /etc/motd
RUN adduser -D admin && echo "admin:admin" | chpasswd && \
    echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel && \
    adduser admin wheel
EXPOSE 22
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
