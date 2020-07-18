#!/bin/bash

RUTA=$1
ACTUAL_DIR=$(pwd)

function backup_dir() {
  FECHA=$(date +%Y-%m-%d:%H:%M:%S)

  7za a "$ACTUAL_DIR"/"$FECHA".7z "$1"
}


function extract() {
  7za x "$1"
}

if [[ -z $1 ]]; then
  echo Es necesaria la ruta absoluta de un fichero o directorio.
  echo se recomienda "$ACTUAL_DIR"/directorio o "$ACTUAL_DIR"/directorio/fichero.txt
  exit 1
fi
if [[ $1 =~ ^\/[^\/] ]] && { [[ -d $1 ]] || [[ -f $1 ]]; }; then
  backup_dir "$RUTA"
else
  echo Es necesaria la ruta absoluta de un fichero o directorio que exista.
  echo se recomienda "$ACTUAL_DIR"/directorio o "$ACTUAL_DIR"/directorio/fichero.txt
  exit 1
fi



