Summary:	OpenSync data synchronization GUI
Summary(pl):	Graficzny interfejs synchronizacji danych OpenSync
Name:		multisync-gui
Version:	0.90.19
Release:	0.1
License:	GPL
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	57bfe0f3375c8d6d5a86cb861d1eeeea
#Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
URL:		http://opensync.org/
BuildRequires:	libopensync-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and distribution
independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains GUI to use OpenSync framework.

%description -l pl
OpenSync to niezale�ny od platformy i dystrybucji szkielet do
synchronizacji danych.

Sk�ada si� z r�nych wtyczek, kt�rych mo�na u�ywa� do ��czenia z
urz�dzeniami, pot�nego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera graficzny interfejs u�ytkownika do korzystania
ze szkieletu OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
