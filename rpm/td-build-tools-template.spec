Name: td-build-tools-template
Version: 0.1.3
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

Requires: %{name}-libexamplelibrary = %{version}-%{release}
Requires: %{name}-example-programs = %{version}-%{release}
Requires: %{name}-example-scripts = %{version}-%{release}


%description
This is a simple example program to be build and packaged by Build Tool.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -ffat-lto-objects"
export CXXFLAGS="%{optflags} -ffat-lto-objects"
export LDFLAGS="%{build_ldflags}"
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DWITH_STATIC_LIBRARIES=ON -DWITH_SHARED_LIBRARIES=ON
%cmake_build

%install
%cmake_install
%find_lang example-program1
%find_lang example-program2
%find_lang example-script1
%find_lang example-script2

# Apply shebang fix for Bash and Rscript:
for directory in %{_bindir} ; do
   find "%{buildroot}/$directory" -type f -exec sed -i \
      -e 's|^#!/usr/bin/env bash|#!/usr/bin/bash|' \
      -e 's|^#!/usr/bin/env python3|#!/usr/bin/python3|' \
      -e 's|^#!/usr/bin/env Rscript|#!/usr/bin/Rscript|' \
      {} +
done

%files -f example-program1.lang -f example-program2.lang -f example-script1.lang -f example-script2.lang


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

%post libexamplelibrary
ldconfig

%postun libexamplelibrary
ldconfig


%package libexamplelibrary-devel
Summary: Development files for example library
Group: Development/Libraries
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description libexamplelibrary-devel
This is a simple example library to be build and packaged by
Build Tool.
This package provides header files for the library.

%files libexamplelibrary-devel
%dir %attr(0755, root, root) %{_includedir}/example
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
%{_datadir}/bash-completion/completions/example-program1
%{_datadir}/bash-completion/completions/example-program2
%{_mandir}/man1/example-program1.1.gz
%{_mandir}/man1/example-program2.1.gz
%dir %attr(0755, root, root) %{_datadir}/doc/build-tools-template
%dir %attr(0755, root, root) %{_datadir}/doc/build-tools-template/examples
%{_datadir}/doc/build-tools-template/examples/example-file1.txt


%package example-scripts
Summary: Example library
BuildArch: noarch
Requires: gettext-runtime
Requires: %{name}-libexamplelibrary = %{version}-%{release}

%description example-scripts
These are simple example scripts and files to be build and packaged by
Build Tool.

%files example-scripts
%{_bindir}/example-script1
%{_bindir}/example-script2
%{_mandir}/man1/example-script1.1.gz
%{_mandir}/man1/example-script2.1.gz
%dir %attr(0755, root, root) %{_datadir}/doc/build-tools-template
%dir %attr(0755, root, root) %{_datadir}/doc/build-tools-template/examples
%{_datadir}/doc/build-tools-template/examples/example-file2.jpeg


%changelog
* Fri Jun 12 2026 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.3-1
- New upstream release.
* Sat Apr 25 2026 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.2-1
- New upstream release.
* Tue Dec 09 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.1-1
- New upstream release.
* Fri Nov 28 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.0-1
- New upstream release.
* Fri Dec 13 2024 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.0.0
- New upstream release.
* Mon Jun 17 2024 Thomas Dreibholz <dreibh@simula.no> - 0.0.0~alpha0
- Created RPM package.
