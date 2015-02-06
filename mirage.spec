Summary:	A fast and simple image viewer
Name:		mirage
Version:	0.9.5.2
Release:	3
Group:		Graphics
License:	GPLv2+
URL:		http://mirageiv.berlios.de/
Source0:	http://download.berlios.de/mirageiv/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(x11)
Requires:	pygtk2.0
Requires:	gnome-python-gconf

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


%changelog
* Tue Jun 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.5.2-1mdv2011.0
+ Revision: 685173
- update to new version 0.9.5.2

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.9.5.1-3
+ Revision: 636093
- tighten BR

* Wed Nov 03 2010 Michael Scherer <misc@mandriva.org> 0.9.5.1-2mdv2011.0
+ Revision: 592726
- rebuild for python 2.7

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.5.1-1mdv2011.0
+ Revision: 567381
- update to new version 0.9.5.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.9.3-4mdv2010.0
+ Revision: 439986
- rebuild

* Mon Dec 29 2008 Michael Scherer <misc@mandriva.org> 0.9.3-3mdv2009.1
+ Revision: 320993
- rebuild for new python

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-2mdv2009.0
+ Revision: 268142
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.3-1mdv2009.0
+ Revision: 194455
- new version

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 159811
- New versino 0.9.2

* Fri Jan 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 147975
- add missing buildrequires on X11-devel
- new version
- do not package COPYING file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-2mdv2008.1
+ Revision: 102480
- fix install
- new version

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.3-3mdv2008.1
+ Revision: 102424
- do not hardcode icon extension in desktop file
- add br on desktop-file-utils
- fix desktop entry

* Mon Sep 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.3-2mdv2008.0
+ Revision: 78837
- correct requires

* Mon Sep 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.3-1mdv2008.0
+ Revision: 78779
- Import mirage

