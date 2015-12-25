%global srcname flower
%global sum A web based tool for monitoring and administrating Celery clusters


Name: python-%{srcname}
Version: 0.8.3
Release: 2%{?dist}
Summary: %{sum}	
License: BSD
URL: https://github.com/mher/%{srcname}
Source0: https://pypi.python.org/packages/source/f/flower/flower-%{version}.tar.gz
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
%autosetup -n %{srcname}-%{version}
rm -r *.egg-info
find . -name '*.py[co]' -delete
rm -r docs/.build


%build
%py3_build
make -C docs html
make -C docs man


%install
%py3_install
install -p -D -T -m 0644 docs/build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/python3-%{srcname}.1
install -p -D -T -m 0644 flower.service %{_unitdir}/%{srcname}.service
# The configuration can contain sensitive information, so lets not have it world-readable.
install -p -D -T -m 0640 flowerconfig.py /etc/flower/flowerconfig.py


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
%{_mandir}/man1/python3-%{srcname}.1*
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%files -n python-%{srcname}-doc
%license LICENSE
%doc docs/build/html/*


%changelog
* Fri Dec 25 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-2
- Remove Python 2 package support. 
- Add docs package.
- Add manpages.

* Thu Nov 26 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-1
- Initial release
