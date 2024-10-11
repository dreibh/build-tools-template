Name: td-build-tools-template
Version: 0.0.0~alpha1
Release: 1
Summary: Build tools example
Group: Applications/Internet
License: GPL-3+
URL: https://www.nntb.no/~dreibh/td-build-tools-template/
Source: https://www.nntb.no/~dreibh/td-build-tools-template/download/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRoot: %{_tmppath}/%{name}-%{version}-build


Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description
This is a simple example program to be build and packaged by Build Tool.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DWITH_STATIC_LIBRARIES=ON -DWITH_SHARED_LIBRARIES=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/example-program1
%{_bindir}/example-program2
%{_mandir}/man1/example-program1.1.gz
%{_mandir}/man1/example-program2.1.gz
%{_datadir}/doc/build-tools-template/examples/example.txt


%package libexamplelibrary
Summary: Example library
Group: System Environment/Libraries
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description libexamplelibrary
This is a simple example library to be build and packaged by
Build Tool.
The example library is provided by this package.

%files libexamplelibrary
%{_libdir}/libexamplelibrary.so.*


%package libexamplelibrary-devel
Summary: Development files for example library
Group: Development/Libraries
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description libexamplelibrary-devel
This is a simple example library to be build and packaged by
Build Tool.
This package provides header files for the library.

%files libexamplelibrary-devel
%{_includedir}/example/library.h
%{_libdir}/libexamplelibrary*.so
%{_libdir}/libexamplelibrary.a


%changelog
* Mon Jun 17 2024 Thomas Dreibholz <dreibh@simula.no> - 0.0.0~alpha0
- Created RPM package.
