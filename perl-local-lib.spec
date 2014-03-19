%define upstream_name    local-lib
%define upstream_version 1.006007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    create and use a local lib/ for perl modules with PERL5LIB
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/local/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Module::Build)
BuildRequires: perl-devel

BuildArch: noarch

Provides: perl(local::lib)

%description
This module provides a quick, convenient way of bootstrapping a user-local
Perl module library located within the user's home directory. It also
constructs and prints out for the user the list of environment variables
using the syntax appropriate for the user's current shell (as specified by
the 'SHELL' environment variable), suitable for directly adding to one's
shell configuration file.

More generally, local::lib allows for the bootstrapping and usage of a
directory containing Perl modules outside of Perl's '@INC'. This makes it
easier to ship an application with an app-specific copy of a Perl module,
or collection of modules. Useful in cases like when an upstream maintainer
hasn't applied a patch to a module of theirs that you need for your
application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# %check
# %make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
