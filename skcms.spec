Summary:	skcms library from skia project
Summary(pl.UTF-8):	Biblioteka skcms z projektu skia
Name:		skcms
Version:	0
%define	gitref	30c8e303800c256febb03a09fdcda7f75d119b1b
%define	snap	20220122
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries
#Source0:	https://skia.googlesource.com/skcms/+archive/%{gitref}.tar.gz?/%{name}-%{snap}.tar.gz
# tarball is regenerated on each download, use distfiles
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	456c87e48d1efc168350714f539893ca
URL:		https://skia.googlesource.com/skcms
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skcms library from skia project.

%description -l pl.UTF-8
Biblioteka skcms z projektu skia.

%package devel
Summary:	Header files for skcms library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki skcms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for skcms library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki skcms.

%package static
Summary:	Static skcms library
Summary(pl.UTF-8):	Statyczna biblioteka skcms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static skcms library.

%description static -l pl.UTF-8
Statyczna biblioteka skcms.

%prep
%setup -q -c

%build
libtool --mode=compile --tag=CXX %{__cxx} %{rpmcxxflags} %{rpmcppflags} -c -o skcms.lo skcms.cc
libtool --mode=link --tag=CXX %{__cxx} %{rpmldflags} %{rpmcxxflags} -o libskcms.la skcms.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

libtool --mode=install install libskcms.la $RPM_BUILD_ROOT%{_libdir}
cp -p skcms.h $RPM_BUILD_ROOT%{_includedir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libskcms.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE 
%attr(755,root,root) %{_libdir}/libskcms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libskcms.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libskcms.so
%{_includedir}/skcms.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libskcms.a
