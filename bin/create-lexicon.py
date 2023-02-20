#!/usr/bin/env python

# create-lexicon.py - given a few configurations, output an edges table

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Februrary 23, 2023 - first cut


# configure
CARREL  = 'liao-presidental_papers-2023'
DEPTH   = 12
BREADTH = 2
SEEDS   = './etc/seeds.txt'

# require
import rdr

# give a list of words, output a set of edges
def seeds2edges( carrel, seeds, topn ) :

	# re-initialize
	nodes = []

	# processs each seed word
	for seed in seeds :

		# search
		results = rdr.word2vec( carrel, type='similarity', query=seed, topn=topn )
		results = results.splitlines()
	
		# process each record
		for result in results :
	
			# parse
			target = result.split( '\t' )[ 0 ]
			weight = result.split( '\t' )[ 1 ]
	
			# output
			print( '\t'.join( [ seed, target, weight ] ) )
		
			# update the list of nodes (new seeds)
			nodes.append( target )

	# done
	return( nodes )


# initialize
with open( SEEDS ) as handle : seeds = handle.read().splitlines()
print( '\t'.join( [ 'source', 'target', 'weight' ] ) )

# do the work a number of times
for index in range( BREADTH ) : seeds = seeds2edges( CARREL, seeds, DEPTH )

# done
exit()
