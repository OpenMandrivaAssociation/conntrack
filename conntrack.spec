%define name conntrack
%define version 1.00
%define beta 2
%if %beta
%define release %mkrel 0.beta%{beta}
%define distname %{name}-%{version}beta%{beta}
%else
%define release %mkrel 1
%define distname %{name}-%{version}
%endif

Summary: Tool to manage the in-kernel connection tracking state table
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://www.netfilter.org/projects/%{name}
BuildRequires: libnetfilter_conntrack-devel

%description
conntrack is a userspace command line program targeted at system
administrators. It enables them to view and manage the in-kernel
connection tracking state table.

Main Features:
* listing the contents of the conntrack table
* searching for individual entries in the conntrack table
* adding new entries to the conntrack table
* listing entries in the expect table
* adding new entries to the expect table

%prep
%setup -q -n %{distname}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.a
%{_libdir}/%{name}/*.la
%{_mandir}/man8/%{name}.8*


