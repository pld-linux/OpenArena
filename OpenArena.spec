%define		_base_ver	0.8.0
#define		_patch_ver	0.7.1
Summary:	OpenArena - a completely free game for the foss Quake III engine
Name:		OpenArena
Version:	%{_base_ver}
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.tuxfamily.org/openarena/rel/%(echo %{_base_ver} | tr -d .)/oa%(echo %{_base_ver} | tr -d .).zip
# Source0-md5:	61aaba81973900d5116a6842079c9c49
URL:		http://openarena.ws/
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%ifarch %{x8664}
# we provide *()(64bit) symbols, so skip hardcoded reqs.
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libSDL-1.2.so.0 libogg.so.0 libopenal.so.0 libvorbis.so.0 libvorbisfile.so.3
%endif

%description
OpenArena for Linux.

%prep
%define __unzip %{_bindir}/unzip -o
%setup -q -n openarena-%{_base_ver}

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
