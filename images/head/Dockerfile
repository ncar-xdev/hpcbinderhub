FROM centos:8.4.2105 AS getter
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget
RUN wget -qO /root/get_port.py https://raw.githubusercontent.com/NERSC/sshspawner/master/scripts/get_port.py

FROM base
RUN dnf install -y openssh-server && \
    dnf clean all
RUN . /opt/conda/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y -c conda-forge jupyterlab dask_labextension nb_conda_kernels && \
    conda clean -y --all
RUN sed -ie "s/#PermitRootLogin.*/PermitRootLogin prohibit-password/g" /etc/ssh/sshd_config && \
    sed -ie "s/#PasswordAuthentication yes/PasswordAuthentication yes/g" /etc/ssh/sshd_config && \
    sed -ie 's/#   Port 22/  Port 22/g' /etc/ssh/sshd_config
COPY --from=getter /root/get_port.py /opt/conda/bin/get_port.py
COPY sshspawner-singleuser /opt/conda/bin/sshspawner-singleuser
CMD [ "/usr/sbin/sshd",  "-D" ]
