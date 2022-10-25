#!/usr/bin/env python

# tsv2csv.py - given a few configurations, output a metadata file suitable for the Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 23, 2022 - first cut; first full day of autumn
# September 24, 2022 - got it working, I think


# configure
SPLITS          = './ppp/splits'
SPLITSPATTERN   = '*.txt'
TSV             = './etc/metadata.tsv'
NAMES           = [ 'id', 'author', 'title', 'begin', 'end', 'url', 'pdf' ]
HEADER          = [ 'author', 'title', 'date', 'file' ]
BASENAMEPATTERN = '-\d\d\d\.txt'

# require
from pathlib import Path
import re
import pandas as pd
import sys

# read and augment the given TSV file
metadata               = pd.read_csv( TSV, sep='\t', names=NAMES )
metadata[ 'basename' ] = metadata[ 'pdf' ].str[ : -4 ].astype( str )
metadata[ 'date' ]     = metadata[ 'begin' ].str[ : 7 ].astype( str )

# get and process each file matching the given pattern; create a list of records
records = []
for index, filename in enumerate( Path( SPLITS ).glob( SPLITSPATTERN ) ) :

	# get the basename (root) of the given file
	file     = str( filename.name )
	basename = re.sub( BASENAMEPATTERN, '', file )
	
	# get the one and only row that matches basename
	row = metadata[ metadata[ 'basename' ] == basename ]
		
	# parse out the author, title, and date values
	author = row[ 'author' ].values[ 0 ]
	title  = row[ 'title' ].values[ 0 ]
	date   = row[ 'date' ].values[ 0 ]

	# update
	record = { 'author':author, 'title':title, 'date':date, 'file':file }
	records.append( record )
		
	# debug
	sys.stderr.write( '     index: ' + str( index ) + '\n' )
	sys.stderr.write( '    author: ' + author       + '\n' )
	sys.stderr.write( '     title: ' + title        + '\n' )
	sys.stderr.write( '      date: ' + str( date )  + '\n' )
	sys.stderr.write( '  filename: ' + file         + '\n' )
	sys.stderr.write( '\n' )
		
# build a new dataframe, output, and done
metadata = pd.DataFrame( records, columns=HEADER )
print( metadata.to_csv( index=False ) )
exit()

	
	
	