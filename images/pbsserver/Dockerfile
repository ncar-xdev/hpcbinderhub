FROM pbsrpms as rpms

FROM base
COPY --from=rpms /root/rpmbuild/RPMS/x86_64/openpbs-server-20.0.1-0.x86_64.rpm /root/
RUN dnf install -y expat libedit postgresql-server postgresql-contrib python3 \
        sendmail sudo tcl tk libical /root/openpbs-server-20.0.1-0.x86_64.rpm && \
    dnf clean all
COPY pbs.conf /etc/pbs.conf
COPY entrypoint.sh .
ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
