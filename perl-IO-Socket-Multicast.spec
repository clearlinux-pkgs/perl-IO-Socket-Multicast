#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-Multicast
Version  : 1.12
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-multicast-perl/libio-socket-multicast-perl_1.12-2.debian.tar.xz
Summary  : Send and receive multicast messages
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Socket-Multicast-lib = %{version}-%{release}
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
Requires: perl-IO-Socket-Multicast-lib = %{version}-%{release}
Provides: perl-IO-Socket-Multicast-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-Multicast package.


%package lib
Summary: lib components for the perl-IO-Socket-Multicast package.
Group: Libraries

%description lib
lib components for the perl-IO-Socket-Multicast package.


%prep
%setup -q -n IO-Socket-Multicast-1.12
cd ..
%setup -q -T -D -n IO-Socket-Multicast-1.12 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Socket-Multicast-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Socket/Multicast.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::Multicast.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/IO/Socket/Multicast/Multicast.so
