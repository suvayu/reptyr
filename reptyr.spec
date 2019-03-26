Name:           reptyr
Version:        0.7.0
Release:        1%{?dist}
Summary:        Reparent a running program to a new terminal
Group:          Applications/System
License:        GPLv3+
URL:            https://github.com/nelhage/reptyr
Source0:        https://github.com/nelhage/reptyr/archive/reptyr-%{version}.tar.gz

# These should be removed in Fedora 26
Provides:       %{name} >= 0.7.0

BuildRequires:  bash-completion
BuildRequires:  gcc

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal. Started a long-running process over
ssh, but have to leave and don't want to interrupt it? Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
make %{?_smp_mflags} PREFIX=/usr

%install
make install PREFIX=/usr DESTDIR=%{buildroot}

%files
%doc ChangeLog COPYING NOTES README.md
%{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*
%{_mandir}/fr/man1/reptyr.1*
%{_datadir}/bash-completion/completions/reptyr

%changelog
* Wed Mar 27 2019 Suvayu Ali <fatkasuvayu+linux@gmail.com> - 0.7.0-1
- new upstream version
