Name: babel
Version: 2.9.0
Release: 0
Summary: An RPM to see if building works.
License: Apache
Group: Productivity
Source: https://github.com/qiaofeng1227/my_rpm/blob/master/SOURCES/Babel-2.9.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: gcc,make,zlib-devel,bzip2-devel
#Requires: 


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

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
