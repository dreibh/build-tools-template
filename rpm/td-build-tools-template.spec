Name: td-build-tools-template
Version: 0.0.0~alpha1
Release: 1
Summary: Build tools example
Group: Applications/System
License: GPL-3.0-or-later
URL: https://www.nntb.no/~dreibh/td-build-tools-template/
Source: https://www.nntb.no/~dreibh/td-build-tools-template/download/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRoot: %{_tmppath}/%{name}-%{version}-build

Requires: %{name}-libexamplelibrary = %{version}-%{release}
Requires: %{name}-example-programs = %{version}-%{release}
Requires: %{name}-example-scripts = %{version}-%{release}


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
%{_includedir}/example/example-library.h
%{_libdir}/libexamplelibrary*.so
%{_libdir}/libexamplelibrary.a


%package example-programs
Summary: Example library
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description example-programs
These are simple example programs and files to be build and packaged by
Build Tool.

%files example-programs
%{_bindir}/example-program1
%{_bindir}/example-program2
%{_datadir}/locale/*/LC_MESSAGES/example-program1.mo
%{_datadir}/locale/*/LC_MESSAGES/example-program2.mo
%{_mandir}/man1/example-program1.1.gz
%{_mandir}/man1/example-program2.1.gz
%{_datadir}/doc/build-tools-template/examples/example-file1.txt


%package example-scripts
Summary: Example library
Requires: gettext-runtime
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description example-scripts
These are simple example scripts and files to be build and packaged by
Build Tool.

%files example-scripts
%{_bindir}/example-script1
%{_bindir}/example-script2
%{_datadir}/locale/*/LC_MESSAGES/example-script1.mo
%{_datadir}/locale/*/LC_MESSAGES/example-script2.mo
%{_mandir}/man1/example-script1.1.gz
%{_mandir}/man1/example-script2.1.gz
%{_datadir}/doc/build-tools-template/examples/example-file2.jpeg


%changelog
* Mon Jun 17 2024 Thomas Dreibholz <dreibh@simula.no> - 0.0.0~alpha0
- Created RPM package.
