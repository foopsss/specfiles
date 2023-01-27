#!/bin/bash

# Descargo los archivos del proyecto.
if [ -d ~/rpmbuild/GIT/shell-color-scripts ]
then
	rm -r -f ~/rpmbuild/GIT/shell-color-scripts
fi
git -C ~/rpmbuild/GIT clone https://gitlab.com/dwt1/shell-color-scripts.git
rm ~/rpmbuild/GIT/shell-color-scripts/PKGBUILD
rm ~/rpmbuild/GIT/shell-color-scripts/.gitlab-ci.yml
rm -r -f ~/rpmbuild/GIT/shell-color-scripts/.git
rm ~/rpmbuild/GIT/shell-color-scripts/man.org

# Creo el archivo tar.
echo -n "Inserte la versión de shell-color-scripts: "
read version

cd ~/rpmbuild/GIT
tar --create --file shell-color-scripts-$version.tar.gz shell-color-scripts
mv shell-color-scripts-$version.tar.gz ~/rpmbuild/SOURCES/shell-color-scripts-$version.tar.gz

# Limpio el directorio donde se almacena el código durante la creación del RPM.
rm -r ~/rpmbuild/BUILDROOT/shell-color-scripts

# Pauso el script para realizar cambios en el archivo spec de ser necesario.
read -n1

# Creo el RPM.
toolbox run -c rpm rpmbuild -v -ba ~/rpmbuild/SPECS/shell-color-scripts.spec
