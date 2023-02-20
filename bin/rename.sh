#!/usr/bin/env bash

# rename.sh - give a few configrations, rename a bunch o' files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Feburary 13, 2023 - first cut; broken and probably needs escaping of some sort


# configure
PATTERN='./corpus/txt/*.txt'
FIND='.pdf'
REPLACE=''

# do the work
rename $FIND $REPLACE $PATTERN

