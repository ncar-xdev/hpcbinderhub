FROM centos:8.4.2105 as rpms
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

FROM centos:8.4.2105
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
COPY --from=rpms /root/rpmbuild/RPMS/x86_64 /root/rpmbuild/RPMS/x86_64
RUN dnf install -y python3 /root/rpmbuild/RPMS/x86_64/openpbs-client-20.0.1-0.x86_64.rpm
RUN groupadd -g 990 cluster && \
    useradd -u 1001 -G cluster alpha && \
    echo "alpha:funkya" | chpasswd && \
    useradd -u 1002 -G cluster beta &&  \
    echo "beta:funkyb" | chpasswd && \
    unlink /var/run/nologin
