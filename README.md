
# Monetary Policy

Given sets of metadata files describing United States Presidential Speeches, output a CSV file (time series data) describing when monetary policy words were used.

## Synopsis

   * `./bin/mods2tsv.sh` - read metadata (MODS) files and create a set of metadata values
   * `./bin/harvset.sh` - given the metadata, download the desired PDF files
   * `./bin/pdf2txt.sh` - convert PDF to plain text
   * `./bin/rename.sh` - clean-up after pdf2txt
   * `./bin/split.sh` - divided the plain text files into something smaller and more managable
   * `./bin/tsv2csv.py` - output a CSV file suitable for the Distant Reader
   * `./bin/create-lexicon.py` - given a few seeds, output an edges table in order to draft a lexicon
   * `./bin/count-lexicon.py` - given a configured lexicon, output a CSV (time series) file

'More to come.
   
---
Eric Lease Morgan &lt;emorgan@nd.edu&gt;   
February 20, 2022
