%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	MethodMaker
Summary:	Class::MethodMaker - a module for creating generic methods
Summary(pl):	Class::MethodMaker - modu� do tworzenia og�lnych metod
Name:		perl-%{pdir}-%{pnam}
Version:	1.06
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl -pi -e 's/5\.00307/5.003_07/' lib/Class/MethodMaker.pm
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
