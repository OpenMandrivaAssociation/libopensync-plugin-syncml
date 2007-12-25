%define name	libopensync-plugin-syncml
%define version	0.35
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	SyncML plugin for opensync synchronization tool
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Obsoletes:	multisync-syncml
Provides:	multisync-syncml
BuildRequires:	opensync-devel >= 0.20
BuildRequires:	libsyncml-devel >= 0.4.2
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise via SyncML

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensynic-1.0/defaults/*
