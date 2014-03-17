%define debug_package %{nil}

Name:           yoshimi
Summary:        ZynAddSubFX with improved RT capacities
Version:        1.1.0
Release:        1

Source:         http://downloads.sourceforge.net/yoshimi/%{name}-%{version}.tar.bz2
URL:            http://yoshimi.sourceforge.net
License:        GPLv2
Group:          Sound
BuildRequires:  cmake libalsa-devel jackit-devel fltk-devel zlib-devel
BuildRequires:  fftw-devel mxml-devel sndfile-devel fontconfig-devel glu-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils

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

%files

%dir %{_datadir}/%name
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop




%changelog
* Sat Jul 07 2012 Frank Kober <emuse@mandriva.org> 1.0.0-2
+ Revision: 808443
+ rebuild (emptylog)

* Thu Jul 05 2012 Frank Kober <emuse@mandriva.org> 1.0.0-1
+ Revision: 808158
- new version 1.0.0

* Thu Jan 05 2012 Frank Kober <emuse@mandriva.org> 0.060.12-1
+ Revision: 757857
- new version 0.060.12
  o svg icon added
- new version 0.060.11
  o fltk-1.3 patch from last commit got applied upstream :)

* Sun Dec 25 2011 Frank Kober <emuse@mandriva.org> 0.060.10-1
+ Revision: 745139
- new version 0.060.10
  o added patch fixing build with fltk 1.3
  o fixed some file permissions

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - rebuild for new fltk

* Mon Apr 04 2011 Frank Kober <emuse@mandriva.org> 0.060.8-1
+ Revision: 650371
- new boost-devel requirement honored
- new version 0.060.8
   o default MIDI backend now JACK MIDI
   o comment added to description

* Thu Jul 15 2010 Frank Kober <emuse@mandriva.org> 0.058.1-1mdv2011.0
+ Revision: 553530
- new version 0.58.1

* Wed Apr 28 2010 Frank Kober <emuse@mandriva.org> 0.056-2mdv2010.1
+ Revision: 539972
- use package optimization instead of optflags

* Sun Apr 11 2010 Frank Kober <emuse@mandriva.org> 0.056-1mdv2010.1
+ Revision: 533600
- sync sources
- new version 0.56, respect bs CCXFLAGS

* Tue Mar 30 2010 Frank Kober <emuse@mandriva.org> 0.055.6-1mdv2010.1
+ Revision: 529978
-restablish definition of BuildRoot
- new version 0.55.6

* Fri Feb 26 2010 Stéphane Téletchéa <steletch@mandriva.org> 0.055.3-1mdv2010.1
+ Revision: 511422
- Another missing BR
- really fix the missing BR
- missing BR

  + Frank Kober <emuse@mandriva.org>
    - import yoshimi



