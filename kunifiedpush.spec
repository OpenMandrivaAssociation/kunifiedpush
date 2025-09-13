%define major 1
%define libname %mklibname kunifiedpush
%define devname %mklibname kunifiedpush -d
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name:		kunifiedpush
Version:	25.08.1
Release:	1
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Library for handling push notifications
URL:		https://invent.kde.org/libraries/kunifiedpush
License:	GPL
Group:		System/Libraries
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	pkgconfig(openssl)

%description
Library for handling push notifications

%package -n %{libname}
Summary:	Library for handling push notifications
Group:		System/Libraries

%description -n %{libname}
Library for handling push notifications

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name},
a library for handling push notifications

%files -f %{name}.lang
%{_bindir}/*
%{_sysconfdir}/xdg/KDE/kunifiedpush-distributor.conf
%{_sysconfdir}/xdg/autostart/org.kde.kunifiedpush-distributor.desktop
%{_prefix}/lib/systemd/user/graphical-session.target.wants/kunifiedpush-distributor.service
%{_prefix}/lib/systemd/user/kunifiedpush-distributor.service
%{_libdir}/plugins/plasma/kcms/systemsettings/kcm_push_notifications.so
%{_datadir}/applications/kcm_push_notifications.desktop
%{_datadir}/qlogging-categories6/org_kde_kunifiedpush.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
