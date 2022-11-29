#!/usr/bin/env python

# count-lexicon.py - given a few configurations, output a CSV file

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 29, 2022 - first investigations
# November  29, 2022 - took stopwords into account and backed out relative scores


# configure
TEXT      = './corpus/txt'
PATTERN   = '*.txt'
LEXICON   = './etc/lexicon.txt'
STOPWORDS = './etc/stopwords-lexicon.txt'
WINDOW    = 80

# require
from pathlib import Path
import pandas as pd
import re
from nltk.tokenize import word_tokenize

# read and normalize the lexicon
with open( LEXICON ) as handle : lexicon = handle.readlines()
lexicon = [ word.strip() for word in lexicon ]
lexicon = [ word.lower() for word in lexicon ]

# get the stop words
with open( STOPWORDS ) as handle : stopwords = handle.readlines()
stopwords = [ word.strip() for word in stopwords ]

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

		# find and process all positions matching the query; finditer does the magic
		matches = re.finditer( '\\b' + item + '\\b', data )
		for match in matches :
	
			# re-initialize
			start = match.start()
			end   = match.end()
		
			# get the characters before and after the item
			before = data[ start - WINDOW : start ]
			after  = data[ end            : end + WINDOW ]

			# build a snippet and tokenize the result
			snippet = before + ' ' + item + ' ' + after
			words   = word_tokenize( snippet )
						
			# process each stop word; check for stopwords
			for stopword in stopwords:
			
				# de-increment and discontinue, conditionally
				if stopword in words :
					count = count - 1
					break
				
		# divide the count by the size of the given file to create relative counts, not
		weight = count / size
		weight = count
		
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

