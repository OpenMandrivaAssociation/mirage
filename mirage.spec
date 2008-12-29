Summary:	A fast and simple image viewer
Name:		mirage
Version:	0.9.3
Release:	%mkrel 3
Group:		Graphics
License:	GPLv2+
URL:		http://mirageiv.berlios.de/
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
BuildRequires:	X11-devel
Requires:	pygtk2.0
Requires:	gnome-python-gconf
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Mirage is a fast and simple GTK+ image viewer. Because it 
depends only on PyGTK, Mirage is ideal for users who wish to 
keep their computers lean while still having a clean image viewer.

%prep
%setup -q
sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{name}.desktop

%build
env CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

# remove document files
rm -f %{buildroot}%{_datadir}/%{name}/[A-Z]*

desktop-file-install \
	--remove-category="Application" \
	--add-category="Viewer" \
	--remove-key="Version" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGELOG README TODO TRANSLATORS
%{_bindir}/%{name}
%{python_sitearch}/%{name}.py*
%{python_sitearch}/*.egg-info
%{python_sitearch}/*.so
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*%{name}.desktop
