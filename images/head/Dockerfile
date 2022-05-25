FROM centos:8.4.2105 AS getter
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget
RUN wget -qO /root/get_port.py https://raw.githubusercontent.com/NERSC/sshspawner/master/scripts/get_port.py

FROM base
RUN dnf install -y openssh-server && \
    dnf clean all
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin no/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config && \
    sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config && \
    sed -ie "s/# Host */Host */g" /etc/ssh/ssh_config && \
    sed -ie "s/#   StrictHostKeyChecking ask/  StrictHostKeyChecking accept-new/g" /etc/ssh/ssh_config && \
    ssh-keygen -A
COPY environment.yml /tmp/
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge mamba && \
    mamba env update --file=/tmp/environment.yml && \
    mamba clean -y --all && \
    rm -rf /tmp/*
COPY --from=getter /root/get_port.py /opt/conda/bin/get_port.py
COPY sshspawner-singleuser /opt/conda/bin/sshspawner-singleuser
CMD [ "/usr/sbin/sshd",  "-D" ]
