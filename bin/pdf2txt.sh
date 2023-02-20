#!/usr/bin/env bash

# pdf2txt.sh - given a few configurations, extract plain text from PDF files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 13, 2023 - first investigations


# configure
PDF='./corpus/pdf'
TXT='./corpus/txt'
TIKA='./lib/tika-app.jar'
CONSUMERS=24

# extract plain text from pdf
java -jar $TIKA -numConsumers $CONSUMERS -t -i $PDF -o $TXT
