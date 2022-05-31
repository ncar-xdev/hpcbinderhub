FROM pbsrpms AS rpms

FROM jupyter as jupyter

FROM base
COPY --from=rpms /root/rpmbuild/RPMS/x86_64openpbs-client-20.0.1-0.x86_64.rpm /tmp/openpbs-client-20.0.1-0.x86_64.rpm
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
RUN sed -ie "s|Defaults    secure_path = .*|Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/opt/conda/condabin:/opt/pbs/bin:opt/pbs/sbin|g" /etc/sudoers
RUN cp /opt/conda/etc/profile.d/conda.sh /etc/profile.d/
USER root
COPY entrypoint.sh /etc/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/etc/entrypoint.sh" ]
