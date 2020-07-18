#!/bin/bash

ACTUAL_DIR=$(pwd)

if [[ -z $1 ]]; then
  echo Es necesario proporcionar un fichero.
  echo se recomienda "$ACTUAL_DIR"/directorio/fichero.txt
  exit 1
fi
if [[ $1 =~ ^\/[^\/] ]] && [[ -f $1 ]]; then
  sed -n -e '12, 22p' "$1"
else
  echo Es necesaria la ruta absoluta de un fichero que exista.
  echo se recomienda "$ACTUAL_DIR"/directorio/fichero.txt
  exit 1
fi
