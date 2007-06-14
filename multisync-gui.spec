Summary:	OpenSync data synchronization GUI
Summary(pl.UTF-8):	Graficzny interfejs synchronizacji danych OpenSync
Name:		multisync-gui
Version:	0.91.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	3760eef2216f3905f21491b6b345d07f
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel > 2:2.6.0
BuildRequires:	libglade2-devel > 1:2.0.1
BuildRequires:	libopensync-devel >= 0.20
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.335
BuildRequires:	waf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains GUI to use OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera graficzny interfejs użytkownika do korzystania ze
szkieletu OpenSync.

%prep
%setup -q

%build
%waf configure \
	--prefix=%{_prefix}
%waf

%install
rm -rf $RPM_BUILD_ROOT
%waf install \
	--destdir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/multisync-gui
%{_desktopdir}/multisync-gui.desktop
%dir %{_datadir}/multisync-gui
%{_datadir}/multisync-gui/multisync-gui.glade
%dir %{_pixmapsdir}/multisync-gui
%{_pixmapsdir}/multisync-gui/multisync.png
