Summary:	Stereo reverb LADSPA plugin
Summary(pl.UTF-8):	Wtyczka LADSPA - stereofoniczny pogłos
Name:		ladspa-g2reverb
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/g2reverb-%{version}.tar.bz2
# Source0-md5:	072c2af1f0ed526be432ede7e7a529ae
Patch0:		%{name}-misc_fixes.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the stereo
reverb effect.

%description -l pl.UTF-8
Ta wtyczka LADSPA zawiera cyfrową implementację stereofonicznego
efektu pogłosu.

%prep
%setup -q -n g2reverb-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/g2reverb.so
