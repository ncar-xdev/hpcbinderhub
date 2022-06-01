FROM pbsrpms AS rpms
FROM jupyter AS jupyter

FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=rpms /root/rpmbuild/RPMS/x86_64/openpbs-client-20.0.1-0.x86_64.rpm /tmp/openpbs-client-20.0.1-0.x86_64.rpm
RUN dnf install -y nano sudo openssh-clients python3 \
        /tmp/openpbs-client-20.0.1-0.x86_64.rpm && \
    dnf clean all && \
    rm -rf /tmp/*
COPY pbs.conf /etc/pbs.conf
RUN sed -i "s|# Host|Host|g" /etc/ssh/ssh_config && \
    sed -i "s|#   StrictHostKeyChecking ask|  StrictHostKeyChecking no|g" /etc/ssh/ssh_config && \
    sed -i "s|#   IdentityFile ~/.ssh/id_rsa|  IdentityFile ~/.ssh/id_rsa|g" /etc/ssh/ssh_config && \
    sed -i "s|#   Port 22|  Port 22|g" /etc/ssh/ssh_config && \
    ssh-keygen -A
RUN groupadd -g 500 admin && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m admin && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin
USER admin
COPY --from=jupyter --chown=admin:admin /opt/jupyter /opt/jupyter
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
RUN sed -ie "s|Defaults    secure_path = .*|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/opt/conda/condabin:/opt/conda/bin:/opt/pbs/bin:/opt/pbs/sbin|g" /etc/sudoers
COPY cluster.sudoers /etc/sudoers.d/cluster
RUN cp /opt/jupyter/etc/profile.d/conda.sh /etc/profile.d/
COPY entrypoint.sh /etc/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/etc/entrypoint.sh" ]
