%define name conntrack
%define version 1.0.0
%define beta 0
%if %beta
%define release %mkrel 0.beta%{beta}
%define distname %{name}-tools-%{version}beta%{beta}
%else
%define release %mkrel 1
%define distname %{name}-tools-%{version}
%endif

Summary: Tool to manage the in-kernel connection tracking state table
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.netfilter.org/projects/conntrack-tools/files/%{distname}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://conntrack-tools.netfilter.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libnetfilter_conntrack-devel >= 0.9.1
BuildRequires: bison
BuildRequires: flex

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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}
install -m644 doc/stats/conntrackd.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS
%{_sbindir}/%{name}
%{_sbindir}/%{name}d
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}d.8*
%{_sysconfdir}/%{name}d.conf


