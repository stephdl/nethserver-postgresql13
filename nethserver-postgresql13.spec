Summary: NethServer PostgresSQL 13.0 configuration
Name: nethserver-postgresql13
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: rh-postgresql13
Requires: nethserver-base

BuildRequires: nethserver-devtools 

%description
NethServer PostgresSQL 13.0 configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed May 19 2021 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial
