Name:           posterazor
Version:        1.9.7
Release:        1%{?dist}
Summary:        Cut an image or PDF into pieces which can be printed and assembled to a poster


License:        MIT
URL:            https://github.com/aportale/posterazor
Source0:        %{name}-master.zip


BuildRequires: qt5-qtbase-devel
BuildRequires: coreutils


%description
Cut an image or PDF into pieces which can be printed and assembled to a poster


%prep
%setup -n posterazor-master


%build
cd src
qmake-qt5 \
    QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
    QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
    posterazor.pro
make


%install
cd src
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 PosteRazor %{buildroot}%{_bindir}/%{name}


%files
/usr/bin/posterazor


%changelog
