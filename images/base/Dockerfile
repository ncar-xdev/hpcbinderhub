FROM centos:8.4.2105 as pbsrpms
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
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
    wget -O openpbs-20.0.1.tar.gz https://github.com/openpbs/openpbs/archive/refs/tags/v20.0.1.tar.gz && \
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
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
RUN dnf install -y wget
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash /tmp/miniconda.sh -b -u -p /opt/conda && \
    cp /opt/conda/etc/profile.d/conda.sh /etc/profile.d/ && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda clean --all

FROM centos:8.4.2105
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=pbsrpms /root/rpmbuild/RPMS/x86_64 /root/rpmbuild/RPMS/x86_64
COPY --from=conda /opt/conda /opt/conda
RUN dnf install -y nano openssh-clients python3 /root/rpmbuild/RPMS/x86_64/openpbs-client-20.0.1-0.x86_64.rpm
COPY pbs.conf /etc/pbs.conf
RUN groupadd -g 990 cluster && \
    useradd -u 1001 -G cluster alpha && \
    echo "alpha:alpha" | chpasswd && \
    useradd -u 1002 -G cluster beta &&  \
    echo "beta:beta" | chpasswd && \
    useradd -u 1003 -G cluster gamma && \
    echo "gamma:gamma" | chpasswd && \
    useradd -u 1004 -G cluster delta &&  \
    echo "delta:delta" | chpasswd && \
    unlink /var/run/nologin
COPY entrypoint.sh /etc/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "/etc/entrypoint.sh" ]
