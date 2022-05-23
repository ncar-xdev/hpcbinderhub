FROM centos:8.4.2105
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN groupadd -g 990 cluster && \
    useradd -u 1001 -G cluster alpha && \
    echo "alpha:funkya" | chpasswd && \
    useradd -u 1002 -G cluster beta &&  \
    echo "beta:funkyb" | chpasswd && \
    unlink /var/run/nologin
