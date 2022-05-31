FROM pbsrpms AS rpms

FROM jupyter
COPY --from=rpms /root/rpmbuild/RPMS/x86_64/openpbs-execution-20.0.1-0.x86_64.rpm /tmp/openpbs-execution-20.0.1-0.x86_64.rpm
RUN dnf install -y expat python3 /tmp/openpbs-execution-20.0.1-0.x86_64.rpm && \
    dnf clean all && \
    rm -rf /tmp/*
COPY pbs.conf /etc/pbs.conf
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT [ "/bin/sh", "/root/entrypoint.sh" ]
