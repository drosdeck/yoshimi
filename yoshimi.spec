%define name    yoshimi
%define version 0.055.6
%define release %mkrel 1 

Name:           %{name} 
Summary:        ZynAddSubFX with improved RT capacities
Version:        %{version} 
Release:        %{release}

Source:         http://sourceforge.net/projects/yoshimi/files/%name-%version.tar.bz2
URL:            http://yoshimi.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
License:        GPLv2
Group:          Sound
BuildRequires:  cmake alsa-lib-devel libjack-devel fltk-devel libz-devel
BuildRequires:  fftw-devel mxml-devel libsndfile-devel fontconfig-devel mesaglu-devel

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone 
synthesizer, but with improved realtime capacities. Yoshimi can use 
either ALSA or JACK for both Audio and MIDI.

%prep
%setup -q
cd src


%build
cd src
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DDEFAULT_MIDI=alsa
%make

%install
rm -rf %buildroot
cd src
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/applications
#make desktop file
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Yoshimi
Comment=The improved ZynAddSubFX synthesizer
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{_datadir}/%name
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/applications/mandriva-%{name}.desktop


