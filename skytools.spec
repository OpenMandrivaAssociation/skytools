Summary:	PostgreSQL database management tools from Skype
Name:		skytools
Version:	2.1.11
Release:	%mkrel 1
License:	BSD
Group:		Databases
Source0:	http://pgfoundry.org/frs/download.php/2370/%{name}-%{version}.tar.gz
URL:		http://pgfoundry.org/projects/skytools
BuildRequires:	postgresql-devel python-devel
Requires:	python-psycopg2 postgresql
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Database management tools from Skype:WAL shipping, queueing, replication. 
The tools are named walmgr, PgQ and Londiste, respectively.

%package	modules
Summary:	PostgreSQL modules of Skytools
Group:		Databases
Requires:	skytools = %{EVRD}

%description	modules
This package has PostgreSQL modules of skytools.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}
%doc %{_docdir}/postgresql/contrib/*
%dir %{python_sitearch}/%{name}
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/upgrade/final/*.sql
%{_datadir}/postgresql/contrib/londiste.sql
%{_datadir}/postgresql/contrib/londiste.upgrade.sql
%{_datadir}/postgresql/contrib/pgq.sql
%{_datadir}/postgresql/contrib/pgq.upgrade.sql
%{_datadir}/postgresql/contrib/pgq_ext.sql
%{_datadir}/postgresql/contrib/uninstall_pgq.sql
%attr(755,root,root) %{_bindir}/*.py
%{python_sitearch}/londiste/*.py*
%{python_sitearch}/pgq/*.py*
%{python_sitearch}/skytools/*.py*
%{python_sitearch}/skytools/_cquoting.so
%{_mandir}/man1/bulk_loader.*
%{_mandir}/man1/cube_dispatcher.*
%{_mandir}/man1/londiste.*
%{_mandir}/man1/pgqadm.*
%{_mandir}/man1/queue_mover.*
%{_mandir}/man1/queue_splitter.*
%{_mandir}/man1/scriptmgr.*
%{_mandir}/man1/skytools_upgrade.*
%{_mandir}/man1/table_dispatcher.*
%{_mandir}/man1/walmgr.*
%{_mandir}/man5/londiste.*
%{python_sitearch}/%{name}-%{version}-py%{pyver}.egg-info

%files modules
%{_libdir}/postgresql/*.so
%{_datadir}/postgresql/contrib/pgq_lowlevel.sql
%{_datadir}/postgresql/contrib/pgq_triggers.sql
%{_datadir}/postgresql/contrib/logtriga.sql

