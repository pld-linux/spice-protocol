Summary:	SPICE protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu SPICE
Name:		spice-protocol
Version:	0.8.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ff6a308c9ff393eb01d0d35b783af7c4
URL:		http://www.spice-space.org/
BuildRequires:	rpmbuild(macros) >= 1.446
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS 
%{_includedir}/spice-1
%{_npkgconfigdir}/spice-protocol.pc