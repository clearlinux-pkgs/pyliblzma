#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyliblzma
Version  : 0.5.3
Release  : 17
URL      : https://pypi.python.org/packages/source/p/pyliblzma/pyliblzma-0.5.3.tar.bz2
Source0  : https://pypi.python.org/packages/source/p/pyliblzma/pyliblzma-0.5.3.tar.bz2
Summary  : Python bindings for liblzma
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
Requires: pyliblzma-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(liblzma)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : xz-dev
Patch1: 0001-Force-usr-bin-python2.patch

%description
PylibLZMA provides a python interface for the liblzma library
to read and write data that has been compressed or can be decompressed
by Lasse Collin's lzma utils.

%package legacypython
Summary: legacypython components for the pyliblzma package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyliblzma package.


%package python
Summary: python components for the pyliblzma package.
Group: Default

%description python
python components for the pyliblzma package.


%prep
%setup -q -n pyliblzma-0.5.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528753879
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
