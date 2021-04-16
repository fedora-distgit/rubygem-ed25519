# Generated from ed25519-1.2.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ed25519

Name: rubygem-%{gem_name}
Version: 1.2.4
Release: 1%{?dist}
Summary: An efficient digital signature library providing the Ed25519 algorithm
License: MIT
URL: https://github.com/crypto-rb/ed25519
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not packaged with the gem. You may get them like so:
# git clone --no-checkout https://github.com/crypto-rb/ed25519
# git -C ed25519 archive -v -o ed25519-1.2.4-spec.txz v1.2.4 spec
Source1: %{gem_name}-%{version}-spec.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/appveyor.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ed25519.gemspec
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/ed25519.png

%changelog
* Fri Apr 16 2021 Pavel Valena <pvalena@redhat.com> - 1.2.4-1
- Initial package
