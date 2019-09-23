%define goroot %{_libdir}/go

Name: packer
Version: 1.4.3
Release: 1%{?dist}
License: MPL2
URL: https://packer.io
Source0: https://github.com/hashicorp/%{name}/archive/v%{version}.tar.gz
BuildRequires: golang

%description
Packer is a tool for building identical machine images for multiple
platforms from a single source configuration.

%prep
%setup -q

%build
go get
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_bindir}/packer

%changelog
* Mon Sep 23 2019 Chris Lamberson <chris@lamberson.online> 1.4.3-1
- initial version
