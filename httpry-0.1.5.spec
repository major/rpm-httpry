Summary: A specialized packet sniffer designed for displaying and logging HTTP traffic
Name: httpry
Version: 0.1.5
Release: 3%{?dist}
License: GPLv2 and BSD
URL: http://dumpsterventures.com/jason/httpry/
Group: Applications/Internet
Source: http://dumpsterventures.com/jason/httpry/httpry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libpcap-devel

%description
httpry is a specialized packet sniffer designed for displaying and logging 
HTTP traffic. It is not intended to perform analysis itself, but to capture, 
parse, and log the traffic for later analysis. It can be run in real-time 
displaying the traffic as it is parsed, or as a daemon process that logs to 
an output file. It is written to be as lightweight and flexible as possible, 
so that it can be easily adaptable to different applications.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -Dp -m 0755 httpry ${RPM_BUILD_ROOT}%{_sbindir}/httpry
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc doc/ChangeLog doc/COPYING doc/format-string doc/method-string doc/perl-tools doc/README 
%{_sbindir}/httpry
%{_mandir}/man1/httpry.1*

%changelog
* Wed Aug 03 2011 Major Hayden <major@mhtx.net> - 0.1.5-3
- Additional cleanup
- Added man page
- Cleaning buildroot to meet EPEL requirements

* Fri Jun 24 2011 Major Hayden <major@mhtx.net> - 0.1.5-2
- Added %{?_smp_mflags} to make

* Fri Jun 24 2011 Major Hayden <major@mhtx.net> - 0.1.5-1
- Initial build
