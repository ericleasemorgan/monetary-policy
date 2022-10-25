#!/usr/bin/env bash

# split.sh - used to divide EB files into smaller chunks

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 4, 2022 - it is a long time coming


# configure
ORIGINALS=/home/emorgan/data/projects/monetary-policy/corpus/txt
SPLITS=/home/emorgan/data/projects/monetary-policy/corpus/splits

# initialize
rm -rf $SPLITS

# find and process each correction
find $ORIGINALS -type f | while read ORIGINAL; do

	# get the basename
	BASENAME=$( basename $ORIGINAL .txt )
	
	# make sane
	mkdir -p $SPLITS
	cd $SPLITS

	# debug, get the base name, and to the work
	echo $ORIGINAL >&2
	split $ORIGINAL $BASENAME- -b 100000 -a 3 -d --additional-suffix=.txt
				
done

