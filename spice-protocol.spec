Summary:	SPICE protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu SPICE
Name:		spice-protocol
Version:	0.12.10
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	1fb9d0dcdd42dce1b476ae8aa7569bcc
URL:		http://www.spice-space.org/
BuildRequires:	python
BuildRequires:	python-pyparsing
BuildRequires:	python-six
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	sed >= 4.0
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

%package codegen
Summary:	SPICE code generator
Summary(pl.UTF-8):	Generator kodu SPICE
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyparsing
Requires:	python-six

%description codegen
SPICE code generator.

%description codegen -l pl.UTF-8
Generator kodu SPICE.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' spice_codegen.py

%build
# use arch-agnostic libdir
%configure \
	--libdir=%{_datadir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/spice-protocol
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/spice-protocol
%py_postclean %{_datadir}/spice-protocol/python_modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS 
%{_includedir}/spice-1
%dir %{_datadir}/spice-protocol
%{_datadir}/spice-protocol/spice.proto
%{_datadir}/spice-protocol/spice1.proto
%{_npkgconfigdir}/spice-protocol.pc

%files codegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/spice-protocol/spice_codegen.py
%{_datadir}/spice-protocol/spice_codegen.py[co]
%dir %{_datadir}/spice-protocol/python_modules
%{_datadir}/spice-protocol/python_modules/*.py[co]
