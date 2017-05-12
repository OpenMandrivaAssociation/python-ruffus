%define module	ruffus

Summary:	Python Computational Pipeline Mgmt
Name:		python-ruffus
Version:	2.6.3
Release:	2
Source0:	http://pybrary.net/%{module}/%{module}-%{version}.tar.gz
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

