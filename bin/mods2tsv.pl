#!/usr/bin/env perl

# mods2tsv.pl - given a MODS file of a specific shape, output a stream of TSV with desired metadata

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 19, 2022 - firsts cut; call me lazy, but ought to be written in Python


# require
use XML::XPath;

# sanity check
my $mods = $ARGV[ 0 ]; 
if ( ! $mods ) { warn "Usage: $0 <mods>\n"; exit }

# initialize
my $parser = XML::XPath->new( filename => $mods );

# parse; magic happens here
my $uri        = ( $parser->find( '/mods/identifier[@type="uri"]' )->get_nodelist )[ 0 ]->string_value;
my $author     = ( $parser->find( '/mods/extension/president/name[@type="authority-lnf"]' )->get_nodelist )[ 0 ]->string_value;
my $title      = ( $parser->find( '/mods/titleInfo/title' )->get_nodelist )[ 0 ]->string_value;
my $dateBegin  = ( $parser->find( '/mods/extension/dateBegin' )->get_nodelist )[ 0 ]->string_value;
my $dateEnd    = ( $parser->find( '/mods/extension/dateEnd' )->get_nodelist )[ 0 ]->string_value;
my $url        = ( $parser->find( '/mods/location/url[@access="raw object"]' )->get_nodelist )[ 0 ]->string_value;

# create short author name
my $shortname = lc( $author );
my @names = split( ', ', $shortname );
my $shortname = @names[ 0 ] . '-' . substr( $names[ 1 ], 0, 1 );

# create filename
my $filename =  $dateBegin . '_' . $dateEnd . '_' . $shortname . '.pdf';

# debug
warn "         uri: $uri\n";
warn "      author: $author\n";
warn "       title: $title\n";
warn "  date begin: $dateBegin\n";
warn "    date end: $dateEnd\n";
warn "         url: $url\n";
warn "   file name: $filename\n";
warn "\n";

# output and done
print( join( "\t", ( $uri, $author, $title, $dateBegin, $dateEnd, $url, $filename ) ), "\n" );
exit;
