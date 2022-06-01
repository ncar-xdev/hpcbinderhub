FROM pbsrpms AS rpms

FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=rpms /root/rpmbuild/RPMS/x86_64/openpbs-server-20.0.1-0.x86_64.rpm /tmp/openpbs-server-20.0.1-0.x86_64.rpm
RUN dnf install -y expat libedit postgresql-server postgresql-contrib python3 \
        sendmail tcl tk libical /tmp/openpbs-server-20.0.1-0.x86_64.rpm && \
    dnf clean all && \
    rm -rf /tmp/*
COPY pbs.conf /etc/pbs.conf
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/root/entrypoint.sh" ]
