%define	_snap	20050717
Summary:	EFL media player written in Ruby
Summary(pl.UTF-8):	Odtwarzacz multimedialny oparty o EFL napisany Rubym
Name:		euphoria
Version:	0.8.0
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	479e7046b4cbd20305ec8009c27b6d65
URL:		http://enlightenment.org/
BuildRequires:	edje
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	ruby-rake
BuildRequires:	sed >= 4.0
Requires:	ruby-ecore
Requires:	ruby-edje
Requires:	ruby-esmart
Requires:	ruby-evas
Requires:	xmms2-client-lib-ecore-ruby
Requires:	xmms2-client-lib-ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFL media player written in Ruby.

%description -l pl.UTF-8
Odtwarzacz multimedialny oparty o EFL napisany Rubym.

%prep
%setup -q -n %{name}
sed -i bin/euphoria \
	-e '/DATA_DIR = /s@".*"@"%{_datadir}/%{name}"@'

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

PREFIX=%{_usr} \
RUBYLIBDIR=%{ruby_sitelibdir} \
DESTDIR=$RPM_BUILD_ROOT \
rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{ruby_sitelibdir}/%{name}
