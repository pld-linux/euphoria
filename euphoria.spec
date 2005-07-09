Summary:	EFL media player written in ruby
Name:		euphoria
Version:	0.8.0
%define	_snap	20050708
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	19adcb18e092ebded5e3f81ded3f8061
URL:		http://enlightenment.org/
BuildRequires:	edje-devel
BuildRequires:	rake
BuildRequires:	ruby-EFL
Requires:	esmart
Requires:	xmms2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitelibdir"]')

%description
EFL media player written in ruby.

%prep
%setup -q -n %{name}

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

DESTDIR=$RPM_BUILD_ROOT
PREFIX=%{_usr}
RUBYLIBDIR=%{_rubylibdir}
export DESTDIR PREFIX RUBYLIBDIR
rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_rubylibdir}/%{name}
