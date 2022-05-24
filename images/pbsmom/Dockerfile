FROM base
RUN dnf install -y --allowerasing expat python3 \
        /root/rpmbuild/RPMS/x86_64/openpbs-execution-20.0.1-0.x86_64.rpm && \
    dnf clean all
COPY entrypoint.sh /root/entrypoint.sh
ENTRYPOINT [ "/bin/sh", "/root/entrypoint.sh" ]
