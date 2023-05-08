#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-Multicast
Version  : 1.12
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-multicast-perl/libio-socket-multicast-perl_1.12-2.debian.tar.xz
Summary  : Send and receive multicast messages
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Socket-Multicast-license = %{version}-%{release}
Requires: perl-IO-Socket-Multicast-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Interface)

%description
NAME
IO::Socket::Multicast - Send and receive multicast messages
SYNOPSIS
use IO::Socket::Multicast;

%package dev
Summary: dev components for the perl-IO-Socket-Multicast package.
Group: Development
Provides: perl-IO-Socket-Multicast-devel = %{version}-%{release}
Requires: perl-IO-Socket-Multicast = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-Multicast package.


%package license
Summary: license components for the perl-IO-Socket-Multicast package.
Group: Default

%description license
license components for the perl-IO-Socket-Multicast package.


%package perl
Summary: perl components for the perl-IO-Socket-Multicast package.
Group: Default
Requires: perl-IO-Socket-Multicast = %{version}-%{release}

%description perl
perl components for the perl-IO-Socket-Multicast package.


%prep
%setup -q -n IO-Socket-Multicast-1.12
cd %{_builddir}
tar xf %{_sourcedir}/libio-socket-multicast-perl_1.12-2.debian.tar.xz
cd %{_builddir}/IO-Socket-Multicast-1.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Socket-Multicast-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Multicast
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Multicast/325afad45103e6403b0eb69e4e5ac2a69291dbd7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::Multicast.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Socket-Multicast/325afad45103e6403b0eb69e4e5ac2a69291dbd7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
