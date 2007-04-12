%define name	libopensync-plugin-syncml
%define version	0.20
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	SyncML plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.opensync.org/plugins/syncml/%{name}-%{version}.tar.gz
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:	libsyncml-devel >= 0.4.2

Obsoletes:	multisync-syncml
Provides:	multisync-syncml

%description
This plugin allows applications using OpenSync to synchronise via SyncML

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


