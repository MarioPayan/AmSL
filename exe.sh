#!/bin/bash

# Para ejecutar el archivo se ejecuta $ sh exe.sh

E="###############################################"
if [ "$#" = "0" ]; then
	echo "\n$E\nLos parametros de entrada son:"
	echo "1) Archivo de texto de entrada"
	echo "2) Archivo de texto de salida (puede omitirlo para ver los resultados en consola)"
	echo "3) Idioma de entrada (es, en)"
	echo "4) Salida (1 pos-tag, 2 morfológico)"
	echo "Ejemplo1) sh exe.sh entrada.txt salida.txt es 1"
	echo "Ejemplo2) sh exe.sh entrada.txt es 2\n$E\n "
	exit
fi

if [  "$#" = "3" ] ; then

	if [ ! "$3" = "es" ] && [ ! "$3" = "en" ]; then
		echo "\n$E\nEl idioma $3 es inválido\n$E\n"
		exit
	fi

	if [ ! -f "$1" ]; then
		echo "\n$E\nNo existe el archivo $1\n$E\n"
		exit
	fi

	if [ "$1" = "$2" ]; then
		echo "\n$E\nEl archivo de entrada no puede ser el mismo de salida (somos rígidos)\n$E\n"
		exit
	fi

	if [ ! -f "$2" ]; then
		echo "\n$E\nNo existe el archivo $2 pero ya lo creamos :3\n$E\n"
		touch "$2"
	fi

	echo "Analizando..."
	analyze -f /usr/local/share/freeling/config/"$3".cfg < "$1" > "$2"
	echo "Finalizado :D"
	exit
fi

if [  "$#" = "2" ] ; then
	if [ ! -f "$1" ]; then
		echo "\n$E\nNo existe el archivo $1\n$E\n"
		exit
	fi

	if [ ! "$2" = "es" ] && [ ! "$2" = "en" ]; then
		echo "\n$E\nEl idioma $2 es inválido\n$E\n"
		exit
	fi

	echo "Analizando...\n"
	analyze -f /usr/local/share/freeling/config/"$2".cfg < "$1"
	echo "Finalizado :D"
	exit
fi

echo "\n$E\nEl número de parametros ingresados es inválido\n$E\n"
exit