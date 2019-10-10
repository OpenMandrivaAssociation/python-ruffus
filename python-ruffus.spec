%define module	ruffus

Summary:	Python Computational Pipeline Mgmt
Name:		python-ruffus
Version:	2.8.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/a1/73/cc66b80cfd495d6ce1e26292776d8f6bb67281bde4f47826b6cb20aa9c87/ruffus-2.8.3.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pybrary.net/pyPdf/
Provides:	%{module}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
The Ruffus module is a lightweight way to add support for running 
computational pipelines.
Computational pipelines are often conceptually quite simple, especially 
if we breakdown the process into simple stages, or separate tasks.
Each stage or task in a computational pipeline is represented by a 
python function Each python function can be called in parallel to run 
multiple jobs.
Ruffus was originally designed for use in bioinformatics to analyse 
multiple genome data sets.


%files
%doc README.rst CHANGES.TXT
%{py_puresitedir}/%{module}-%{version}-py%{py_ver}.egg-info
%dir %{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --no-compile

