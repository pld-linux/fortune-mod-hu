Summary:	Collection of Hungarian fortunes
Summary(pl):	Zestaw w�gierskich fortunek
Name:		fortune-mod-hu
Version:	0.1
Release:	1
License:	Public Domain
Group:		Applications/Games
Requires:	fortune-mod
Source0:	http://melkor.dnp.fmph.uniba.sk/~garabik/fortunes-hu/fortunes-hu.tar.gz
# Source0-md5:	88bf0718b8e5eab8f582be90b510c9bc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l pl
Fortune-mod zawiera wci�� popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochot� na odrobin� m�dro�ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog� doda� fortune do plik�w .login u�ytkownik�w tak,
by ka�dy otrzyma� swoj� dawk� m�dro�ci przy logowaniu.

%prep
%setup -q -n fortunes-hu

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install hu/* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
