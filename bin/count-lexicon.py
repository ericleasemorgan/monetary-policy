#!/usr/bin/env python

# count-lexicon.py - given a few configurations, output a CSV file

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 29, 2022 - first investigations


# configure
TEXT    = './corpus/txt'
PATTERN = '*.txt'
LEXICON = './etc/lexicon.txt'

# require
from pathlib import Path
import pandas as pd
import re

# read and normalize the lexicon
with open( LEXICON ) as handle : lexicon = handle.readlines()
lexicon = [ word.strip() for word in lexicon ]
lexicon = [ word.lower() for word in lexicon ]

# process each file in the given configuration; create a list of rows
rows = []
for file in Path( TEXT ).glob( PATTERN ) :

	# derive a key; not very elegant
	key   = str( file.name )
	parts = key.split( '_' )
	key   = '_'.join( [ parts[ 0 ], parts[ 1 ] ] )
	
	# slurp up the file
	with open( file ) as handle : data = handle.read().lower()
	
	# get the size of the file, measured in words (more or less, mostly more)
	size = len( data.split() )	
	
	# re-initialize a row
	row = [ key ]
	
	# process each word in the given lexicon
	for item in lexicon :
	
		# count the number of times the lexicon item is found in the data
		count = data.count( item )
		
		# divide the count by the size of the given file to create a relative counts
		weight = count / size
		
		# update the row
		row.append( weight )
	
	# update the rows
	rows.append( row )

# build a header
header = lexicon
header.insert( 0, 'dates' )

# combine the rows and header into a dataframe
counts = pd.DataFrame( rows, columns=header )

# output and done
print( counts.to_csv( index=False ) )
exit()

