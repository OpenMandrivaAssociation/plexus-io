Name:		plexus-io
Version:	3.4.0
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
BuildRequires:	plexus-pom
BuildRequires:	plexus-utils
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(javax.inject:javax.inject)
# provided scope: sources import javax.annotation, and Maven still resolves it
BuildRequires:	mvn(com.google.code.findbugs:jsr305)
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
Input, output, and file-selection helpers shared by Plexus components.
3.4.0 is the last release that still builds against Plexus Utils 3.
IncludeExcludeFileSelector, which the Maven Javadoc plugin imports, is
in this jar.

%prep
%autosetup -n plexus-io-plexus-io-%{version}

%files -f .mfiles
%doc NOTICE.txt README.md ReleaseNotes.md
