Name     : jdk-eclipse-eclipse
Version  : 3.6.0.v20100505
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/eclipse/org.eclipse.eclipse/3.6.0.v20100505/org.eclipse.eclipse-3.6.0.v20100505.pom
Source0  : http://repo.maven.apache.org/maven2/org/eclipse/org.eclipse.eclipse/3.6.0.v20100505/org.eclipse.eclipse-3.6.0.v20100505.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/eclipse-eclipse.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/eclipse-eclipse.xml \
%{buildroot}/usr/share/maven-poms/eclipse-eclipse.pom \
%{buildroot}/usr/share/java/eclipse-eclipse.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-poms/eclipse-eclipse.pom
/usr/share/maven-metadata/eclipse-eclipse.xml
