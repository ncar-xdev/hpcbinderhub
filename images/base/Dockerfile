FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y nano sudo openssh-clients && \
    dnf clean all && \
    rm -rf /tmp/*
RUN groupadd -g 500 admin && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m admin && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin
USER admin
RUN mkdir ~/.ssh && \
    ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa && \
    ssh-keygen -s ~/.ssh/id_rsa -I admin -n admin ~/.ssh/id_rsa.pub && \
    cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys
USER root
RUN groupadd -g 990 cluster && \
    useradd -u 1001 -G cluster alpha && \
    echo "alpha:alpha" | chpasswd && \
    useradd -u 1002 -G cluster beta &&  \
    echo "beta:beta" | chpasswd && \
    useradd -u 1003 -G cluster gamma && \
    echo "gamma:gamma" | chpasswd
COPY cluster.sudoers /etc/sudoers.d/cluster
