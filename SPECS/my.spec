Name: Python
Version: 3.8.7
Release: 0
Summary: An RPM to see if building works.
License: Apache
Group: Productivity
Source: https://github.com/qiaofeng1227/my_rpm/blob/master/SOURCES/test.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: gcc,make,zlib-devel,bzip2-devel
Requires: build-essential,libssl-dev,zlib1g-dev,libbz2-dev,libreadline-dev,libsqlite3-dev,wget,curl,llvm,libncurses5-dev,libncursesw5-dev,xz-utils,tk-dev,libffi-dev,liblzma-dev


%description
Build a mock RPM.

%prep
%setup -q

%build
./configure
make

%install
make install

%files
%defattr(-,root,root,-)

%changelog
