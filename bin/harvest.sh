#!/usr/bin/env bash

# harvest.sh - given a few configurations, cache remote PDF files locally

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 19, 2022 - firsts cut


# configure
TSV='./etc/metadata.tsv'
PDF='./corpus/pdf'
JOBS='./tmp/jobs.tsv'
PROCESSES=5

# make sane
mkdir -p $PDF
mkdir -p $TMP
rm -rf $JOBS
IFS=$'\t'

# process each metadata record
cat $TSV | while read URI AUTHOR TITLE BEGIN END URL FILE; do

	# update
	FILE=$PDF/$FILE
	
	# debug
	echo "   url: $URL"  >&2
	echo "  file: $FILE" >&2 
	echo ""              >&2 
	
	# update the list of jobs, conditionally
	if [[ ! -f $FILE ]]; then echo "wget $URL -O $FILE" >> $JOBS; fi
	
done

# do the work in parallel and done
cat $JOBS | parallel --jobs $PROCESSES
exit
