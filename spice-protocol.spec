Summary:	SPICE protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu SPICE
Name:		spice-protocol
Version:	0.14.2
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz
# Source0-md5:	a8db4b8a02ed87074cba56967fcad6c8
URL:		https://www.spice-space.org/
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files defining the SPICE protocol.

The Spice project aims to provide a complete open source solution for
interaction with virtualized desktop devices.

%description -l pl.UTF-8
Pliki nagłówkowe protokołu SPICE.

Celem projektu Spice jest dostarczenie pełnego, mającego otwarte
źródła rozwiązania do interakcji z wirtualizowanymi urządzeniami
biurkowymi.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{_includedir}/spice-1
%{_npkgconfigdir}/spice-protocol.pc
