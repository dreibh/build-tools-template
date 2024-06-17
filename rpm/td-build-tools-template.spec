Name: td-build-tools-template
Version: 0.0.0~alpha0
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
BuildRoot: %{_tmppath}/%{name}-%{version}-build

# TEST ONLY:
# define _unpackaged_files_terminate_build 0


%description
This is a simple example program to be build and packaged by Build Tool.

%prep
%setup -q

%build
# NOTE: CMAKE_VERBOSE_MAKEFILE=OFF for reduced log output!
# NOTE: ENABLE_BACKEND_MARIADB=OFF, since mysql-connector-c++ is not provided by Fedora.
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DWITH_STATIC_LIBRARIES=ON -DWITH_SHARED_LIBRARIES=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}example
%{_mandir}/man1/example.1.gz
%{_datadir}/doc/td-build-tools-template/examples/example.txt


%package libexample
Summary: Example library
Group: System Environment/Libraries
Requires: %{name}-libexample = %{version}-%{release}

%description libexample
This is a simple example library to be build and packaged by
Build Tool.
The example library is provided by this package.

%files libexample
%{_libdir}/libexample.so.*


%package libexample-devel
Summary: Development files for example library
Group: Development/Libraries
Requires: %{name}-libexample = %{version}-%{release}

%description libexample-devel
This is a simple example library to be build and packaged by
Build Tool.
This package provides header files for the library.

%files libexample-devel
%{_includedir}/example/library.h
%{_libdir}/libexample*.so
%{_libdir}/libexample.a


%changelog
