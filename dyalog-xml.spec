%define name	dyalog-xml
%define version 1.0.3
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DyAlog XML module
License:	GPL
Group:		Sciences/Computer science
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{name}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#dyalog-xml
BuildRequires:	dyalog
BuildRequires:	libxml2-devel
ExclusiveArch:  %{ix86}

%description
A DyALog module providing predicates over LibXML API. This module, while very
preliminary, may be used to read, process and print XML documents with DyALog.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	libxml2-devel
Requires:	%{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q

%build
export CPPFLAGS=-I%{_libdir}/DyALog
export LDFLAGS=-L%{_libdir}/DyALog
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_libdir}/DyALog/%{name}/%{name}.pc %{buildroot}%{_libdir}/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README
%{_libdir}/DyALog/%{name}

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/%{name}.pc

