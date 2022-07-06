FROM pbsrpms AS rpms
FROM conda AS conda

FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=rpms /root/rpmbuild/RPMS/x86_64/openpbs-client-20.0.1-0.x86_64.rpm /tmp/openpbs-client-20.0.1-0.x86_64.rpm
RUN dnf install -y git nano sudo openssh-clients podman python3 \
        /tmp/openpbs-client-20.0.1-0.x86_64.rpm && \
    dnf clean all && \
    rm -rf /tmp/* /root/*
COPY registries.conf /etc/containers/registries.conf
COPY storage.conf /etc/containers/storage.conf
RUN echo 'user.max_user_namespaces=127357' > /etc/sysctl.d/01-maxusernamespaces.conf && \
    echo 'alpha:100000:65536' >> /etc/subuid && \
    echo 'alpha:100000:65536' >> /etc/subgid && \
    echo 'beta:100000:65536' >> /etc/subuid && \
    echo 'beta:100000:65536' >> /etc/subgid && \
    echo 'gamma:100000:65536' >> /etc/subuid && \
    echo 'gamma:100000:65536' >> /etc/subgid
COPY pbs.conf /etc/pbs.conf
RUN ssh-keygen -A && \
    mkdir ~/keys && \
    ssh-keygen -q -t rsa -N '' -f ~/keys/certauth && \
    ssh-keygen -q -t rsa -N '' -f ~/keys/client && \
    ssh-keygen -s ~/keys/certauth -I jupyter -n jupyter ~/keys/client.pub && \
    cp ~/keys/client /etc/ssh/ && \
    cp ~/keys/client-cert.pub /etc/ssh/
COPY ssh_config /etc/ssh/ssh_config.d/cluster.conf
RUN groupadd -g 500 admin && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m admin && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    chmod +r /etc/ssh/client* && \
    unlink /var/run/nologin
COPY --from=conda --chown=admin:admin /opt/conda /opt/conda
RUN groupadd -g 990 cluster && \
    useradd -u 1001 -G cluster alpha && \
    echo "alpha:alpha" | chpasswd && \
    useradd -u 1002 -G cluster beta && \
    echo "beta:beta" | chpasswd && \
    useradd -u 1003 -G cluster gamma && \
    echo "gamma:gamma" | chpasswd
RUN sed -ie "s|Defaults    secure_path = .*|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/opt/conda/condabin:/opt/conda/bin:/opt/pbs/bin:/opt/pbs/sbin|g" /etc/sudoers
COPY cluster.sudoers /etc/sudoers.d/cluster
RUN cp /opt/conda/etc/profile.d/conda.sh /etc/profile.d/
COPY entrypoint.sh /etc/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/etc/entrypoint.sh" ]
