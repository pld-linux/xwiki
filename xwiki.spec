# NOTE:
# - it is yet another maven-based project. Don't try tu build it from sources.
#   Don't waste your time.
# - it is nosrc, because sources are quite large, and I don't know to fetch
#   them to DF until it works.

Summary:	A second generation wiki
Summary(pl.UTF-8):	Wiki drugiej generacji.
Name:		xwiki
Version:	2.0.3
Release:	0.1
License:	LGPL
Group:		Networking/Daemons/Java/Servlets
# Sources:
# http://download.forge.objectweb.org/xwiki/xwiki-enterprise-web-2.0.3.war
# http://download.forge.objectweb.org/xwiki/xwiki-enterprise-wiki-2.0.3.xar
Source0:	%{name}-enterprise-web-%{version}.war
# NoSource0-md5:	722dc5be34cde8f6b40d59a1cc04da21
NoSource:	0
Source1:	%{name}-enterprise-wiki-%{version}.xar
# NoSource1-md5:	98a9045df7ce58bd7b438a7db140adc8
NoSource:	1
Source2:	%{name}-context.xml
URL:		http://www.xwiki.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	tomcat >= 0:6.0.20-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XWiki is a platform for developing collaborative web applications
using the wiki paradigm. This is what makes XWiki a second generation
wiki.

%description -l pl.UTF-8
XWiki jest platformą na bazie której można budować aplikacje
spełniające paradygmat wiki. To sprawia, że XWiki jest wiki drugiej
generacji.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},/var/log/%{name}}


cp -a . $RPM_BUILD_ROOT%{_datadir}/%{name}

# configuration
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_sharedstatedir}/tomcat/conf/Catalina/localhost}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
ln -s %{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tomcat-context.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/tomcat-context.xml
%config(noreplace) %verify(not md5 mtime size) %attr(2775,root,tomcat) %{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
