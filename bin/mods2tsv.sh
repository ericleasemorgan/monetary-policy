#!/usr/bin/env bash

# mods2tsv.sh - a front-end to mod2tsv.pl

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 19, 2022 - firsts cut


# configure
MODS='./corpus/mods'
MODS2TSV='./bin/mods2tsv.pl'
TSV='./etc/metadata.tsv'

# find and parallel process each MODS file and done
find $MODS -type f | parallel $MODS2TSV > $TSV
exit
