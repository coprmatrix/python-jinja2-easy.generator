#
# spec file for package python-jinja2-easy.generator
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-jinja2-easy.generator
Version:        0.0.1
Release:        0
Summary:        Jinja2 easy generator
License:        GPL-3.0-only
URL:            https://github.com/huakim/python-jinja2_easy
Source:         jinja2_easy_generator-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module platformdirs}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jinja2
Requires:       python-platformdirs
BuildArch:      noarch
%python_subpackages

%description
Jinja2 easy generator

%prep
%autosetup -p1 -n jinja2_easy.generator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files  %{python_files}
%{python_sitelib}/jinja2_easy/
%{python_sitelib}/jinja2_easy.generator-%{version}.dist-info/



%changelog
