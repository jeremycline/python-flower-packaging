%global srcname flower
%global sum A web based tool for monitoring and administrating Celery clusters


Name: python-%{srcname}
Version: 0.8.3
Release: 2%{?dist}
Summary: %{sum}	
License: BSD
URL: https://github.com/mher/%{srcname}
Source0: https://pypi.python.org/packages/source/f/flower/flower-%{version}.tar.gz
# Fixes a test in 0.8.3 that has already been fixed in upstream's master branch.
Patch0: pool_reset_test_fix.patch
Source1: flower.service
Source2: flowerconfig.py
BuildArch: noarch


%description
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%package -n python3-%{srcname}
Summary: %{sum}
Requires: python3-celery >= 2.5.0
Requires: python3-tornado >= 4.0.0
Requires: python3-babel
Requires: python3-pytz
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%package -n python-%{srcname}-doc
Summary: %{sum}
BuildRequires: python-celery >= 2.5.0
BuildRequires: python-tornado >= 4.0.0
BuildRequires: python-babel
BuildRequires: pytz
BuildRequires: python-sphinx
BuildRequires: python-futures
BuildRequires: python-sphinxcontrib-fulltoc
BuildRequires: python-sphinxcontrib-httpdomain

%description -n python-%{srcname}-doc
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.

This package contains the documentation for Flower.


%prep
%setup -n %{srcname}-%{version} -q
%patch0 -p0
rm -r *.egg-info
find . -name '*.py[co]' -delete
rm -r docs/.build


%build
%py3_build
make %{?_smp_mflags} -C docs html
make %{?_smp_mflags} -C docs man
rm docs/.build/html/.buildinfo


%install
%py3_install
install -p -D -T -m 0644 docs/.build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{srcname}.service
install -p -D -T -m 0644 %{SOURCE2} %{buildroot}/etc/%{srcname}/config.py


%check
%{__python3} setup.py test


%post
%systemd_post %{srcname}.service

%preun
%systemd_preun %{srcname}.service

%postun
%systemd_postun_with_restart %{srcname}.service


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS CHANGES
%{_mandir}/man1/%{srcname}.1*
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info
%{_unitdir}/%{srcname}.service
%config(noreplace) /etc/%{srcname}/config.py*


%files -n python-%{srcname}-doc
%license LICENSE
%doc docs/.build/html/*


%changelog
* Fri Dec 25 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-2
- Remove Python 2 package support. 
- Add docs package.
- Add manpages.
- Add check section.
- Add patch to fix a failing test in 0.8.3

* Thu Nov 26 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-1
- Initial release
