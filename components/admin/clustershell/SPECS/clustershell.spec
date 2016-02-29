%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:          clustershell
Version:       1.7
Release:       6%{?dist}
Summary:       Python framework for efficient cluster administration

Group:         System Environment/Base
License:       CeCILL-C
URL:           http://clustershell.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%if 0%{?suse_version} == 1110
BuildArch:     x86_64
%else
#%%if 0%%{?fedora} 
BuildArch:     noarch
%endif

BuildRequires: python-devel python-setuptools

%description
Tools and event-based Python library to execute commands on cluster nodes in
parallel depending on selected engine and worker mechanisms. The library
provides also advanced NodeSet and NodeGroups handling methods to ease and
improve administration of large compute clusters or server farms. Three
convenient command line utilities, clush, clubak and nodeset, allow traditional
shell scripts to benefit some useful features offered by the library.

%package -n vim-%{name}
Summary:       VIM files for ClusterShell
Group:         System Environment/Base
Requires:      clustershell = %{version}-%{release}, vim-common

%description -n vim-%{name}
Syntax highlighting in the VIM editor for ClusterShell configuration files.


%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --prefix=%{_prefix} --skip-build --root %{buildroot}

# config files
install -d %{buildroot}/%{_sysconfdir}/clustershell/groups.conf.d
install -d %{buildroot}/%{_sysconfdir}/clustershell/groups.d
install -p -m 0644 conf/*.conf %{buildroot}/%{_sysconfdir}/clustershell/
install -p -m 0644 conf/groups.conf.d/*.conf.example %{buildroot}/%{_sysconfdir}/clustershell/groups.conf.d

# man pages
install -d %{buildroot}/%{_mandir}/{man1,man5}
install -p -m 0644 doc/man/man1/clubak.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/clush.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/nodeset.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man5/clush.conf.5 %{buildroot}/%{_mandir}/man5/
install -p -m 0644 doc/man/man5/groups.conf.5 %{buildroot}/%{_mandir}/man5/

# vim addons
%define vimdatadir %{_datadir}/vim/vimfiles
install -d %{buildroot}/%{vimdatadir}/{ftdetect,syntax}
install -p -m 0644 doc/extras/vim/ftdetect/clustershell.vim %{buildroot}/%{vimdatadir}/ftdetect/
install -p -m 0644 doc/extras/vim/syntax/clushconf.vim %{buildroot}/%{vimdatadir}/syntax/
install -p -m 0644 doc/extras/vim/syntax/groupsconf.vim %{buildroot}/%{vimdatadir}/syntax/


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog Licence_CeCILL-C_V1-en.txt Licence_CeCILL-C_V1-fr.txt
%doc doc/examples
%{_mandir}/man1/clubak.1*
%{_mandir}/man1/clush.1*
%{_mandir}/man1/nodeset.1*
%{_mandir}/man5/clush.conf.5*
%{_mandir}/man5/groups.conf.5*
%dir /usr%{_sysconfdir}/clustershell
%{_sysconfdir}/clustershell/clush.conf
%{_sysconfdir}/clustershell/groups.conf
%config(noreplace) /usr%{_sysconfdir}/clustershell/clush.conf
%config(noreplace) /usr%{_sysconfdir}/clustershell/groups.conf
%dir /usr%{_sysconfdir}/clustershell/groups.conf.d
%dir /usr%{_sysconfdir}/clustershell/groups.d
%doc /usr%{_sysconfdir}/clustershell/groups.conf.d/*.conf.example
%{python_sitelib}/ClusterShell/
%{python_sitelib}/ClusterShell-*-py?.?.egg-info
%{_bindir}/clubak
%{_bindir}/clush
%{_bindir}/nodeset

%files -n vim-%{name}
%defattr(-,root,root,-)
%dir %{_datadir}/vim/
%dir %{vimdatadir}
%dir %{vimdatadir}/ftdetect
%dir %{vimdatadir}/syntax
%{vimdatadir}/ftdetect/clustershell.vim
%{vimdatadir}/syntax/clushconf.vim
%{vimdatadir}/syntax/groupsconf.vim

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6-5
- Use special %%doc to install docs (#993703).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Stephane Thiell <stephane.thiell@cea.fr> 1.6-1
- update to 1.6

* Thu Jun 09 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.5.1-1
- update to 1.5.1

* Wed Jun 08 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.5-1
- update to 1.5

* Sat Mar 19 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.4.3-1
- update to 1.4.3

* Tue Mar 15 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.4.2-1
- update to 1.4.2

* Sun Feb 13 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.4.1-1
- update to 1.4.1

* Sat Jan 15 2011 Stephane Thiell <stephane.thiell@cea.fr> 1.4-1
- update to 1.4

* Wed Oct 20 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3.3-1
- update to 1.3.3

* Fri Sep 10 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3.2-1
- renamed Vim subpackage to vim-clustershell
- update to 1.3.2

* Sun Sep 05 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3.1-2
- added -vim subpackage for .vim files

* Fri Sep 03 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3.1-1
- removed -n from setup line
- own clustershell config directory for proper uninstall
- install vim syntax addons in vimfiles, thus avoiding vim version detection
- update to 1.3.1

* Sun Aug 22 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3-4
- fixed BuildRoot tag in accordance with EPEL guidelines
- python_sitelib definition: prefer global vs define
- preserve timestamps and fix permissions when installing files

* Sat Aug 21 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3-3
- use a full URL to the package in Source0

* Fri Aug 20 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3-2
- various improvements per first review request

* Thu Aug 19 2010 Stephane Thiell <stephane.thiell@cea.fr> 1.3-1
- initial build candidate for Fedora

