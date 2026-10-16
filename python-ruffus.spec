%define module	ruffus

Summary:	Python computational pipeline management
Name:		python-ruffus
Version:	3.0.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/ruffus/
Source0:	https://files.pythonhosted.org/packages/source/r/ruffus/ruffus-%{version}.tar.gz
Provides:	%{module}
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
The Ruffus module is a lightweight way to add support for running
computational pipelines. Each stage is a Python function, and each
function can run several jobs in parallel.

3.0.0 requires Python 3.11 or newer. Checkpoint history paths are
relative to the database directory, and keyword-only defaults affect
function checksums, so an existing pipeline reruns affected jobs once.

%files
%doc README.rst CHANGES.TXT LICENSE.TXT
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
