#!/usr/bin/env python3
from taxadb.taxid import TaxID
import fileinput
taxid = TaxID(dbtype='sqlite', dbname='taxadb.sqlite')
for line in fileinput.input():
    try:
        taxid = int(line)
        lineage = taxid.lineage_name(taxid)
        print(lineage)
    except:
        pass
