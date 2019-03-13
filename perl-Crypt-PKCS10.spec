#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	PKCS10
Summary:	Crypt::PKCS10 - parse PKCS #10 certificate requests
Summary(pl.UTF-8):	Crypt::PKCS10 - parsowanie żądań certyfikatu w formacie PKCS #10
Name:		perl-Crypt-PKCS10
Version:	2.001
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	07f2f79978b4ca11de9bcdc4269a3ab1
URL:		http://search.cpan.org/dist/Crypt-PKCS10/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	openssl
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Crypt::PKCS10 parses PKCS #10 certificate requests (CSRs) and provides
accessor methods to extract the data in usable form. Common object
identifiers will be translated to their corresponding names.
Additionally, accessor methods allow extraction of single data fields.
The format of returned data varies by accessor. The access methods
return the value corresponding to their name. If called in scalar
context, they return the first value (or an empty string). If called
in array context, they return all values. true values should be
specified as 1 and false values as 0. Future API changes may provide
different functions when other values are used.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/PKCS10.pm
%{_mandir}/man3/Crypt::PKCS10.3*
