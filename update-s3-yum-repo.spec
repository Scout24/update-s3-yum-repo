Name: update-s3-yum-repo
Summary: Maintain YUM Repository in S3 Bucket
Version: __VERSION__
Release: 1__EXTRAREV__
Group: IS24
License: GPL
Source: %{name}-%{version}.tar.gz
Requires: awscli, procmail, createrepo, yum-utils, python-magic
BuildArch: noarch

%description
Download given S3 bucket, add RPM to it, do repo maintenance, rebuild repo metadata and upload again

%prep
%setup

%install
mkdir -p %{buildroot}/var/cache/update-s3-yum-repo %{buildroot}/usr/bin
install -m 0755 update-s3-yum-repo -t %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/*
%attr(1777,-,-) /var/cache/update-s3-yum-repo

