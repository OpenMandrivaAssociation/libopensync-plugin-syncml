%define name	libopensync-plugin-syncml
%define version	0.33
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	SyncML plugin for opensync synchronization tool
License:	LGPL
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Obsoletes:	multisync-syncml
Provides:	multisync-syncml
BuildRequires:	opensync-devel >= 0.20
BuildRequires:	libsyncml-devel >= 0.4.2
BuildRequires:	scons
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise via SyncML

%prep
%setup -q

%build
scons prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=%{buildroot}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


