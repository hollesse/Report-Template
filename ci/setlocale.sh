#!/usr/bin/env sh

# Compile German locale
sudo locale-gen de_DE.UTF-8

# List all locale-files
locale -a

# Set German locale
LANG=de_DE.utf8