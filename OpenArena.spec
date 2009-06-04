# TODO:
# - FHS
# - build from sources; we can't distribute GPLed binaries alone anyway
Summary:	OpenArena - a completely free game for the foss Quake III engine
Summary(pl.UTF-8):	OpenArena - darmowa gra wykorzystująca silnik Quake III
Name:		OpenArena
Version:	0.8.1
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.tuxfamily.org/openarena/rel/%(echo %{version} | tr -d .)/oa%(echo %{version} | tr -d .).zip
# Source0-md5:	49006bcb02b4e8ea3d06749e8f4e4887
URL:		http://openarena.ws/
BuildRequires:	unzip
# applies to this binary distribution only
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenArena for Linux.

%description -l pl.UTF-8
OpenArena dla Linuksa.

%prep
%define __unzip %{_bindir}/unzip -o
%setup -q -n openarena-%{version}

cat << 'EOF' > openarena
#/bin/sh
exec /opt/OpenArena/openarena
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/opt/OpenArena/{baseoa,missionpack},%{_bindir}}

install baseoa/*.pk3 $RPM_BUILD_ROOT/opt/OpenArena/baseoa
install missionpack/*.pk3 $RPM_BUILD_ROOT/opt/OpenArena/missionpack
install openarena.%{_target_base_arch} $RPM_BUILD_ROOT/opt/OpenArena/openarena
install openarena $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%attr(755,root,root) %{_bindir}/openarena
%dir /opt/OpenArena
%attr(755,root,root) /opt/OpenArena/openarena
/opt/OpenArena/baseoa
/opt/OpenArena/missionpack
