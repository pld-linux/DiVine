Summary:	DirectFB Virtual Input extension
Summary(pl.UTF-8):	Rozszerzenie DirectFB o wirtualne wejście
Name:		DiVine
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}.tar.gz
# Source0-md5:	6c1147d186e421f707afd48403749364
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= 1:1.2.0
BuildRequires:	pkgconfig >= 1:0.9
%requires_eq	DirectFB
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DiVine consists of:
- an input driver that reads raw input events from a pipe and
  dispatches them via a virtual input device.
- a library that handles the connection to the input driver including
  helper functions for generating events.
- a tool called "spooky" to generate input events using a simple
  script featuring button or motion events, linear or circular
  automated motion and delays.


%description -l pl.UTF-8
DiVine składa się z:
- sterownika wejścia czytającego surowe zdarzenia wejściowe z potoku
  i przekazującego je poprzez wirtualne urządzenie wejściowe,
- biblioteki obsługującej połączenie ze sterownikiem wejściowym oraz
  zawierającej funkcje pomocnicze do generowania zdarzeń,
- narzędzia "spooky" generującego zdarzenia wejściowe przy użyciu
  prostego skryptu oferującego zdarzenia związane z przyciskami i
  ruchem, automatycznym ruchem liniowym lub cyklicznym i opóźnieniami.

%package devel
Summary:	Header files for divine library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki divine
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:1.0.0

%description devel
Header files for divine library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki divine.

%package static
Summary:	Static divine library
Summary(pl.UTF-8):	Statyczna biblioteka divine
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static divine library.

%description static -l pl.UTF-8
Statyczna biblioteka divine.

%prep
%setup -q

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/spooky
%attr(755,root,root) %{_libdir}/libdivine-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdivine-0.4.so.0
%attr(755,root,root) %{_libdir}/directfb-1.2-0/inputdrivers/libdirectfb_divine.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/divine-config
%attr(755,root,root) %{_libdir}/libdivine.so
%{_libdir}/libdivine.la
%{_includedir}/divine
%{_pkgconfigdir}/divine.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdivine.a
%{_libdir}/directfb-1.2-0/inputdrivers/libdirectfb_divine.[aol]*