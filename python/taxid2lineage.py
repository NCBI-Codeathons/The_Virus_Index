#!/usr/bin/env python3
from taxadb.taxid import TaxID
import fileinput
taxid = TaxID(dbtype='sqlite', dbname='taxadb.sqlite')
for line in fileinput.input():
	print(line)
	lineage = taxid.lineage_name(int(line))
	print(lineage)
