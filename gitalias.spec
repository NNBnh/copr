%global srcname gitalias

Name: gitalias
Summary: Git alias commands for faster easier version control.
Version: 1.0.0
Release: 1%{?dist}
License: Unlicense
URL: https://github.com/GitAlias/gitalias
Source0: https://raw.githubusercontent.com/GitAlias/gitalias/main/gitalias.txt
BuildArch: noarch

%description
Git Alias is a collection of git version control alias settings that can help
you work faster and better. Git Alias provides short aliases such as `s` for
status, command aliases such as `chart` and `churn`,lookup aliases such as
`whois` and `whatis`, workflow aliases such as `topic-begin` for feature branch
development, and more.

%prep
%autosetup

%install
%{__install} -D %{_builddir}/gitalias.txt -t %{buildroot}%{_datadir}/gitalias.txt

%files
%{_datadir}/gitalias.txt
