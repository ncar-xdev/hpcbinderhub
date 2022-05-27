FROM centos:8.4.2105 as pbsrpms
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y dnf-plugins-core && \
    dnf config-manager --set-enabled powertools && \
    dnf install -y gcc make rpm-build libtool libtool-ltdl-devel hwloc-devel \
        libX11-devel libXt-devel libedit-devel libical-devel \
        ncurses-devel perl postgresql-devel postgresql-contrib python3-devel tcl-devel \
        tk-devel swig expat-devel openssl-devel libXext libXft \
        autoconf automake gcc-c++ wget && \
    dnf clean all
RUN cd /tmp && \
    wget -qO openpbs-20.0.1.tar.gz https://github.com/openpbs/openpbs/archive/refs/tags/v20.0.1.tar.gz && \
    tar -xpvf openpbs-20.0.1.tar.gz && \
    cd openpbs-20.0.1 && \
    ./autogen.sh && \
    ./configure --prefix=/opt/pbs && \
    make dist
RUN cd /tmp/openpbs-20.0.1 && \
    mkdir /root/rpmbuild /root/rpmbuild/SOURCES /root/rpmbuild/SPECS && \
    mv openpbs-*.tar.gz /root/rpmbuild/SOURCES/ && \
    cp openpbs.spec /root/rpmbuild/SPECS/ && \
    cp openpbs-rpmlintrc /root/rpmbuild/SOURCES/ && \
    cd /root/rpmbuild/SPECS && \
    rpmbuild -ba openpbs.spec

FROM centos:8.4.2105 as conda
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/conda && \
    cp /opt/conda/etc/profile.d/conda.sh /etc/profile.d/ && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda clean --all

FROM centos:8.4.2105
RUN sed -i 's|mirrorlist|#mirrorlist|g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=pbsrpms /root/rpmbuild/RPMS/x86_64 /root/rpmbuild/RPMS/x86_64
RUN dnf install -y nano sudo openssh-clients python3 \
        /root/rpmbuild/RPMS/x86_64/openpbs-client-20.0.1-0.x86_64.rpm && \
    dnf clean all && \
    rm -rf /tmp/*
COPY pbs.conf /etc/pbs.conf
RUN ln -s /usr/bin/python3.6 /usr/bin/python && \
    ln -s /usr/bin/pip3.6 /usr/bin/pip && \
    ln -s /usr/bin/pydoc3.6 /usr/bin/pydoc && \
    ln -s /usr/bin/pyvenv-3.6 /usr/bin/pyvenv
RUN groupadd -g 500 jupyter && \
    groupadd -g 501 shadow && \
    useradd -g 500 -u 500 -G shadow -m jupyter && \
    chgrp shadow /etc/shadow && \
    chmod 0440 /etc/shadow && \
    unlink /var/run/nologin
COPY --from=conda --chown=jupyter:jupyter /opt/conda /opt/conda
RUN groupadd -g 990 jupyterhub && \
    useradd -u 1001 -G jupyterhub alpha && \
    echo "alpha:alpha" | chpasswd && \
    useradd -u 1002 -G jupyterhub beta &&  \
    echo "beta:beta" | chpasswd && \
    useradd -u 1003 -G jupyterhub gamma && \
    echo "gamma:gamma" | chpasswd
RUN sed -i "s|# Host|Host|g" /etc/ssh/ssh_config && \
    sed -i "s|#   StrictHostKeyChecking ask|  StrictHostKeyChecking no|g" /etc/ssh/ssh_config && \
    sed -i "s|#   IdentityFile ~/.ssh/id_rsa|  IdentityFile ~/.ssh/id_rsa|g" /etc/ssh/ssh_config && \
    sed -i "s|#   Port 22|  Port 22|g" /etc/ssh/ssh_config && \
    ssh-keygen -A
RUN sed -ie "s|Defaults    secure_path = .*|Defaults    secure_path = Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/opt/conda/condabin:/opt/pbs/bin:opt/pbs/sbin|g" /etc/sudoers
RUN cp /opt/conda/etc/profile.d/conda.sh /etc/profile.d/
USER jupyter
RUN mkdir ~/.ssh && \
    ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa && \
    ssh-keygen -s ~/.ssh/id_rsa -I jupyter -n jupyter ~/.ssh/id_rsa.pub && \
    cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys
USER root
COPY entrypoint.sh /etc/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/etc/entrypoint.sh" ]
