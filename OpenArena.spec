%define		_base_ver	0.7.0
%define		_patch_ver	0.7.1
Summary:	OpenArena - a completely free game for the foss Quake III engine
Name:		OpenArena
Version:	%{_patch_ver}
Release:	0.1
License:	GPL v2
Group:		Applications/Games
# precompiled archives can be downloaded from website.
Source0:	oa%(echo %{_base_ver} | sed -e 's:\.::g').zip
# Source0-md5:	739548bfc5dc1d129d20c0f67d54df48
Source1:	oa%(echo %{_patch_ver} | sed -e 's:\.::g')-patch.zip
# Source1-md5:	5fa31998009f8241ad3ded93eb81e701
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
%setup -q -n openarena-%{_base_ver} -b1

cat << 'EOF' > ioquake3
#/bin/sh
exec /opt/OpenArena/ioquake3
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/opt/OpenArena/baseoa,%{_bindir}}

install baseoa/*.pk3 $RPM_BUILD_ROOT/opt/OpenArena/baseoa
install ioquake3-smp.%{_target_base_arch} $RPM_BUILD_ROOT/opt/OpenArena/ioquake3
install ioquake3 $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS
%attr(755,root,root) %{_bindir}/ioquake3
%dir /opt/OpenArena
%attr(755,root,root) /opt/OpenArena/ioquake3
/opt/OpenArena/baseoa
