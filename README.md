
# Monetary Policy

Given sets of metadata files describing United States Presidential Speeches, output a CSV file (time series data) describing when monetary policy words were used.

## Synopsis

   * `./bin/mods2tsv.sh` - read metadata (MODS) files and create a set of metadata values
   * `./bin/harveset.sh` - given the metadata, download the desired PDF files
   * `java -jar tika-app.jar` - manually convert the PDF to plain text
   * `./bin/split.sh` - divided the plain text files into something smaller and more managable
   * `./bin/count-lexicon.py` - given a configured lexicon, output a CSV (time series) file

'More to come.
   
---
Eric Lease Morgan &lt;emorgan@nd.edu&gt;   
October 25, 2022
