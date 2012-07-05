%define name    yoshimi
%define version 1.0.0
%define release 1

Name:           %{name}
Summary:        ZynAddSubFX with improved RT capacities
Version:        %{version}
Release:        %{release}

Source:         http://sourceforge.net/projects/yoshimi/files/%name-%version.tar.bz2
URL:            http://yoshimi.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
License:        GPLv2
Group:          Sound
BuildRequires:  cmake libalsa-devel jackit-devel fltk-devel zlib-devel
BuildRequires:  fftw-devel mxml-devel sndfile-devel fontconfig-devel mesaglu-devel
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

rm -f %{buildroot}%{_datadir}/%{name}/banks/chip/.bankdir
chmod -R 755 %{buildroot}%{_datadir}/%{name}/banks
chmod -R 755 %{buildroot}%{_datadir}/%{name}/presets
chmod a-X %{buildroot}%{_datadir}/%{name}/banks/*/*
chmod a-X %{buildroot}%{_datadir}/%{name}/presets/*

desktop-file-install \
    --remove-key="Version" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{_datadir}/%name
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


