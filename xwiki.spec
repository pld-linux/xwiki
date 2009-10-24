# NOTE:
# - it is yet another maven-based project. Don't try tu build it from sources.
#   Don't waste your time.
# - it is nosrc, because sources are quite large, and I don't know to fetch
#   them to DF until it works.

%include	/usr/lib/rpm/macros.java
Summary:	xwiki
Name:		xwiki
Version:	4.0
Release:	0.1
License:	LGPL
Group:		Networking/Daemons/Java/Servlets
# Sources:
# http://download.forge.objectweb.org/xwiki/xwiki-enterprise-web-2.0.2.war
# http://download.forge.objectweb.org/xwiki/xwiki-enterprise-wiki-2.0.2.xar
Source0:	xwiki-enterprise-web-2.0.2.war
# NoSource0-md5:	1313d8284621f35d40e04cecf3787e6a
NoSource:	0
Source1:	xwiki-enterprise-wiki-2.0.2.xar
# NoSource1-md5:	5a760d6d534221745b54acbe09ea51ed
NoSource:	1
#Source2:	%{name}-context.xml
URL:		http://www.atlassian.com/software/jira/default.jsp
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	tomcat >= 0:6.0.20-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xwiki

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},/var/log/%{name}}


cp -a . $RPM_BUILD_ROOT%{_datadir}/%{name}

# configuration
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/jira,%{_sharedstatedir}/tomcat/conf/Catalina/localhost}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sharedstatedir}/tomcat/conf/Catalina/localhost/jira.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/jira/tomcat-context.xml
%config(noreplace) %verify(not md5 mtime size) %attr(2775,root,tomcat) %{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
