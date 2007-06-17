%define		module BitVector
Summary:	A pure-Python memory-efficient packed representation for bit arrays
Summary(pl.UTF-8):	Czysto Pythonowa, efektywna pamięciowo reprezentacja tablic bitów
Name:		python-BitVector
Version:	1.3
Release:	0.9
License:	Python Software Foundation
Group:		Libraries
Source0:	http://rvl4.ecn.purdue.edu/~kak/dist/%{module}-%{version}.tar.bz2
# Source0-md5:	c74c9b4b34296249c766f0f4e7960be2
URL:		http://cobweb.ecn.purdue.edu/~kak/dist/junk.html
BuildRequires:	python-devel
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This class presents a pure-Python memory efficient packed
representation for bit arrays.

%description -l pl.UTF-8
Ta klasa prezentuje czysto Pythonową, efektywną pamięciowo
reprezentację dla tablic bitów.

%prep
%setup -q -n  %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/BitVector.py[co]
%{py_sitescriptdir}/*.egg-info
