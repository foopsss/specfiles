#!/bin/bash

DIRIN=~/rpmbuild/SPECS
DIROUT=$HOME/Documentos/GitHub/Specfiles

for file in $DIRIN/* ; do
	filext=${file##*/}
	filewoext=${filext%.*}
	
	if [ ! -e "$DIROUT/$filewoext" ]
	then
		mkdir "$DIROUT/$filewoext"
	fi
	cp -r "$DIRIN"/$filext "$DIROUT/$filewoext"
done
