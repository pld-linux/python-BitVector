%define		module BitVector
Summary:	A pure-Python memory-efficient packed representation for bit arrays
Summary(pl.UTF-8):	Czysto pythonowa, efektywna pamięciowo reprezentacja tablic bitów
Name:		python-BitVector
Version:	1.5.1
Release:	0.1
License:	Python Software Foundation
Group:		Libraries
Source0:	http://rvl4.ecn.purdue.edu/~kak/dist/%{module}-%{version}.tar.bz2
# Source0-md5:	460a0c164bee3b4582db4ad453e33d3b
URL:		http://cobweb.ecn.purdue.edu/~kak/dist/junk.html
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class presents a pure-Python memory efficient packed
representation for bit arrays.

%description -l pl.UTF-8
Ta klasa prezentuje czysto pythonową, efektywną pamięciowo
reprezentację dla tablic bitów.

%package examples
Summary:        Examples for BitVector module
Summary(pl.UTF-8):      Przykłady użycia modułu BitVector
Group:          Libraries/Python
Requires:       %{name} = %{version}-%{release}

%description examples
This package contains examples for BitVector module.

%description examples -l pl.UTF-8
Pakiet zawierający przykłady użycia modułu BitVector.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/BitVector.py[co]
%{py_sitescriptdir}/*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
