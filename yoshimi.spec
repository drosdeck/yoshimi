%define name    yoshimi
%define version 0.060.12
%define release 1

Name:           %{name}
Summary:        ZynAddSubFX with improved RT capacities
Version:        %{version}
Release:        %{release}

Source:         http://sourceforge.net/projects/yoshimi/files/%name-%version.tar.bz2
Source1:        Bot_galego.svg
URL:            http://yoshimi.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
License:        GPLv2
Group:          Sound
BuildRequires:  cmake alsa-lib-devel jackit-devel fltk-devel libz-devel
BuildRequires:  fftw-devel mxml-devel libsndfile-devel fontconfig-devel mesaglu-devel
BuildRequires:  boost-devel

%description
Yoshimi is the legendary and powerful ZynAddSubFX multitimbral standalone
synthesizer, but with improved realtime capacities. Yoshimi can use
either ALSA or JACK for both Audio and MIDI, the default now being JACK

%prep
%setup -q

%build
cd src
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make

%install
rm -rf %buildroot
cd src
%makeinstall_std
chmod -R a+X %{buildroot}%{_datadir}/%{name}/banks
chmod a-X %{buildroot}%{_datadir}/%{name}/banks/*/*
mkdir -p %{buildroot}%{_datadir}/applications
#make desktop file
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Yoshimi
Comment=The improved ZynAddSubFX synthesizer
Exec=%{_bindir}/%{name}
Icon=Bot_galego
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
EOF

install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{_datadir}/%name
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/icons/hicolor/scalable/apps/Bot_galego.svg
%{_datadir}/applications/mandriva-%{name}.desktop


