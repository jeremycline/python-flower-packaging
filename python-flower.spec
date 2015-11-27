%global srcname flower
%global sum A web based tool for monitoring and administrating Celery clusters


Name: python-%{srcname}
Version: 0.8.3
Release: 1%{?dist}
Summary: %{sum}	
License: BSD
URL: https://github.com/mher/%{srcname}
Source0: https://pypi.python.org/packages/source/f/flower/flower-%{version}.tar.gz
# Patch0: systemd-service.patch
BuildArch: noarch
BuildRequires: python2-devel python3-devel
# BuildRequires: systemd
# Requires(post): systemd
# Requires(preun): systemd
# Requires(postun): systemd


%description
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%package -n python2-%{srcname}
Summary: %{sum}
Requires: python-celery >= 2.5.0
Requires: python2-certifi
Requires: python-futures
Requires: python-backports-ssl_match_hostname
Requires: python-tornado >= 4.0.0
Requires: python-babel
Requires: pytz
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%package -n python3-%{srcname}
Summary: %{sum}
Requires: python3-celery >= 2.5.0
Requires: python3-tornado >= 4.0.0
Requires: python3-babel
Requires: python3-pytz
# python3-kombu, a dep of kombu, should be requiring this
Requires: python3-anyjson
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/*.egg-info
# %{_unitdir}/celery-flower.service


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info
# %{_unitdir}/celery-flower.service


# %post
# %systemd_post celery-flower.service

# %preun
# %systemd_preun celery-flower.service

# %postun
# %systemd_postun_with_restart celery-flower.service


%changelog
* Thu Nov 26 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-1
- Initial release
