#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	MethodMaker
Summary:	Class::MethodMaker - a module for creating generic methods
Summary(pl):	Class::MethodMaker - modu� do tworzenia og�lnych metod
Name:		perl-Class-MethodMaker
Version:	2.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8fa59f63025596a9ca1f6ab9986bd561
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module solves the problem of having to write a bazillion get/set
methods that are all the same.  The argument to 'use' is a hash whose
keys are the names of types of generic methods generated by
MethodMaker and whose values tell method maker what methods to make.
(More precisely, the keys are the names of MethodMaker methods
(methods that write methods) and the values are the arguments to those
methods.

%description -l pl
Ten modu� rozwi�zuje problem pisania bazylion�w metod get/set, kt�re
s� wszystkie takie same. Parametrem 'use' jest hasz, kt�rego klucze s�
nazwami typ�w do og�lnych metod, wygenerowanych przez MethodMakera, a
warto�ci m�wi� modu�owi, kt�re metody utworzy� (bardziej precyzyjnie:
klucze s� nazwami metod MethodMakera (metod, kt�re tworz� metody), a
warto�ci to parametry dla tych metod).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -pi -e 's/5\.00307/5.003_07/' lib/Class/MethodMaker.pm
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%dir %{perl_vendorlib}/auto/%{pdir}
%{perl_vendorlib}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
