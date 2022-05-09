%global _empty_manifest_terminate_build 0
Name:		python-hstspreload
Version:	2020.12.22
Release:	2
Summary:	Chromium HSTS Preload list as a Python package
License:	BSD-3
URL:		https://github.com/sethmlarson/hstspreload
Source0:	https://files.pythonhosted.org/packages/a3/54/ae7e2f9f95abafdec7fbc09b0185a5f44dfacd2da9f303d61e84dbfc30a3/hstspreload-2020.12.22.tar.gz
BuildArch:	noarch


%description
This form is used to submit domains for inclusion in Chrome's HTTP Strict Transport Security(HSTS) 
preload list. This is a list of sites that are hardcoded into Chrome as being HTTPS only.

%package -n python3-hstspreload
Summary:	Chromium HSTS Preload list as a Python package
Provides:	python-hstspreload
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-hstspreload
This form is used to submit domains for inclusion in Chrome's HTTP Strict Transport Security(HSTS)
preload list. This is a list of sites that are hardcoded into Chrome as being HTTPS only.

%package help
Summary:	Development documents and examples for hstspreload
Provides:	python3-hstspreload-doc
%description help
Development documents and examples for hstspreload

%prep
%autosetup -n hstspreload-2020.12.22

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-hstspreload -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue May 17 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 2020.12.22-2
- fix build issue

* Sun May 23 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
