Name: Python
Version: 3.8.7
Release: 0
Summary: An RPM to see if building works.
License: Apache
Group: Productivity
URL: https://robertdebock.nl/
Source: https://github.com/qiaofeng1227/my_rpm/blob/master/SOURCES/test.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: gcc make

%description
Build a mock RPM.

%prep
%setup -q

%build
make

%install
make PREFIX=/usr DESTDIR=%{?buildroot} install

%files
%defattr(-,root,root,-)
%{_bindir}/my

%changelog
