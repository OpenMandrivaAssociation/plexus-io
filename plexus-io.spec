Name:		plexus-io
Version:	3.8.1
Release:	1
Summary:	Plexus IO components
Group:		Development/Java
License:	ASL 2.0
URL:		https://codehaus-plexus.github.io/plexus-io/
Source0:	https://github.com/codehaus-plexus/plexus-io/archive/refs/tags/plexus-io-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	plexus-pom >= 27
BuildRequires:	mvn(org.codehaus.plexus:plexus:pom::)
BuildRequires:	plexus-utils >= 3.6.2
BuildRequires:	apache-commons-io >= 1:2.22.0
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(javax.inject:javax.inject)
# provided scope: sources import javax.annotation, and Maven still resolves it
BuildRequires:	mvn(com.google.code.findbugs:jsr305)
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
Input, output, and file-selection helpers shared by Plexus components.
3.8.1 builds against Plexus Utils 3.6.2. IncludeExcludeFileSelector,
which the Maven Javadoc plugin imports, is in this jar.

Since 3.4.0 the library caches Unix user and group names, follows
symbolic links to files when that is requested, closes the deferred
stream that holds large file contents, and reports a hard-link
identity for resources whose bytes were not transformed. 3.8.1
applies the default excludes with the platform separator. The
manifest names the automatic module
org.codehaus.plexus.components.io.

%prep
%autosetup -n plexus-io-plexus-io-%{version}

%files -f .mfiles
%doc NOTICE.txt README.md
