Summary:	Pngnq is a tool for quantizing PNG images in RGBA format
Name:		pngnq
Version:	1.0
Release:	1
License:	BSD with advertising and MIT and BSD
Group:		Applications/Multimedia
URL:		http://pngnq.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pngnq/%{name}-%{version}.tar.gz
# Source0-md5:	2d2cdacf0284477c662fee888c8092d5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pngnq is a tool for quantizing PNG images in RGBA format.

The neuquant algorithm uses a neural network to optimise the color map
selection. This is fast and quite accurate, giving good results on
many types of images.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
