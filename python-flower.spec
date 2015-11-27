%global srcname flower
%global sum A web based tool for monitoring and administrating Celery clusters


Name: python-%{srcname}
Version: 0.8.3
Release: 1%{?dist}
Summary: %{sum}	
License: BSD
URL: https://github.com/mher/%{srcname}
Source0: https://pypi.python.org/packages/source/f/flower/flower-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel python3-devel


%description
A web based tool for monitoring and administrating Celery clusters. It offers
real-time monitoring using Celery events, remote control of workers and tasks,
broker monitoring, and an HTTP API.


%package -n python2-%{srcname}
Summary: %{sum}
Requires: python-celery >= 2.5.0
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


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Thu Nov 26 2015 Jeremy Cline <jeremy@jcline.org> 0.8.3-1
- Initial release
