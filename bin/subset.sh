#!/usr/bin/env bash

mkdir -p policy
rdr search ppp -q 'bernanke OR "central bank" OR "consumer price index" OR "cost of living" OR cpi OR "federal reserve" OR "gas prices" OR greenspan OR inflation OR "monetary policy" OR "price stability" OR yellen' -o tsv | while read FILE DATA; do
cp $(rdr get)/ppp/txt/$FILE.txt ./policy
done
