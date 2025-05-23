Summary:	SPICE protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu SPICE
Name:		spice-protocol
Version:	0.14.5
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz
# Source0-md5:	53bfb120525a23a795b5faf134fc1dc7
URL:		https://www.spice-space.org/
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{_includedir}/spice-1
%{_npkgconfigdir}/spice-protocol.pc
