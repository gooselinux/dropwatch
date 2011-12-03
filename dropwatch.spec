Summary: Kernel dropped packet monitor 
Name: dropwatch 
Version: 1.2
Release: 0%{?dist} 
Source0: https://fedorahosted.org/releases/d/r/dropwatch/dropwatch-%{version}.tbz2
URL: http://fedorahosted.org/dropwatch
License: GPLv2+ 
Group: Applications/System 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libnl-devel, readline-devel, kernel-headers
BuildRequires: binutils-devel
Requires: libnl, readline

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%setup -q

%build
cd src
export CFLAGS=$RPM_OPT_FLAGS
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0755 src/dropwatch $RPM_BUILD_ROOT%{_bindir}
install -m0644 doc/dropwatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc README
%doc COPYING

%changelog
* Wed Jun 30 2010 Neil Horman <nhorman@redhat.com> - 1.2-0
- Updated to latest upstream to fix segfault (bz581815)

* Wed Apr 14 2010 Neil Horman <nhorman@redhat.com> - 1.1-2
- Fixing up buildRequires

* Tue Apr 03 2010 Neil Horman <nhorman@redhat.com> - 1.1-1
- Bumping release number

* Tue Apr 03 2010 Neil Horman <nhorman@redhat.com> - 1.1-0
- Updating to latest upstream version (bz 581815)

* Fri Mar 20 2009 Neil Horman <nhorman@redhat.com> 1.0-2
- Fixed up Errors found in package review (bz 491240)

* Tue Mar 17 2009 Neil Horman <nhorman@redhat.com> 1.0-1
- Initial build

