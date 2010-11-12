#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	MethodMaker
Summary:	Class::MethodMaker - a module for creating generic methods
Summary(pl.UTF-8):	Class::MethodMaker - moduł do tworzenia ogólnych metod
Name:		perl-Class-MethodMaker
Version:	2.15
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7af92ddaee49815ade7c5886b74d5e64
URL:		http://search.cpan.org/dist/Class-MethodMaker/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module solves the problem of having to write a bazillion get/set
methods that are all the same. The argument to 'use' is a hash whose
keys are the names of types of generic methods generated by
MethodMaker and whose values tell method maker what methods to make.
(More precisely, the keys are the names of MethodMaker methods
(methods that write methods) and the values are the arguments to those
methods.

%description -l pl.UTF-8
Ten moduł rozwiązuje problem pisania bazylionów metod get/set, które
są wszystkie takie same. Parametrem 'use' jest hasz, którego klucze są
nazwami typów do ogólnych metod, wygenerowanych przez MethodMakera, a
wartości mówią modułowi, które metody utworzyć (bardziej precyzyjnie:
klucze są nazwami metod MethodMakera (metod, które tworzą metody), a
wartości to parametry dla tych metod).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv -f t/0-signature.t{,.blah}
mv -f end.pod lib/Class/MethodMaker/

%build
%{__perl} generate.PL
%{__perl} -MExtUtils::MakeMaker -wle \
	'WriteMakefile(NAME=>"Class::MethodMaker",
	PL_FILES=>{}, VERSION=>"%{version}")' \
	INSTALLDIRS=vendor

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Class/.placeholder
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Class/MethodMaker/end.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Class/cmmg.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Class/*.pm
%dir %{perl_vendorarch}/Class/MethodMaker
%{perl_vendorarch}/Class/MethodMaker/*.pm
%dir %{perl_vendorarch}/auto/Class/MethodMaker
%{perl_vendorarch}/auto/Class/MethodMaker/array
%{perl_vendorarch}/auto/Class/MethodMaker/hash
%{perl_vendorarch}/auto/Class/MethodMaker/scalar
%dir %{perl_vendorarch}/auto/Class/MethodMaker/Engine
%{perl_vendorarch}/auto/Class/MethodMaker/Engine/*.al
%{perl_vendorarch}/auto/Class/MethodMaker/Engine/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Class/MethodMaker/*.so
%{perl_vendorarch}/auto/Class/MethodMaker/MethodMaker.bs
%{_mandir}/man3/*
