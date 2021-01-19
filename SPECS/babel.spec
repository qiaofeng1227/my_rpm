Name:sqlite-autoconf		
Version:3340000	
Release:	1%{?dist}
Summary:slqite3 is a db	

#Group:		
License:GPL			
URL:            https://github.com/qiaofeng1227/%{name}
Source0:        https://github.com/qiaofeng1227/my_rpm/blob/master/sqlite-autoconf-3340000.tar.gz

BuildRequires: gcc make
#Requires:	

%description
A simple RPM package to print Hello World

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