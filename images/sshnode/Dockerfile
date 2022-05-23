FROM centos:latest
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y openssh-server openssh-clients && \
    dnf clean all
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin no/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config && \
    sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config && \
    sed -ie "s/# Host */Host */g" /etc/ssh/ssh_config && \
    sed -ie "s/#   StrictHostKeyChecking ask/  StrictHostKeyChecking accept-new/g" /etc/ssh/ssh_config && \
    ssh-keygen -A && \
    unlink /var/run/nologin
RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -G jupyterhub alpha && \
    echo "alpha:funkyduck" | chpasswd && \
    useradd -u 1002 -G jupyterhub beta &&  \
    echo "beta:funkybird" | chpasswd
EXPOSE 22/tcp
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
