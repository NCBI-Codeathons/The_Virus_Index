#!/usr/bin/env python3
from taxadb.taxid import TaxID
import fileinput
taxid = TaxID()
for line in fileinput.input():
    try:
        t = int(line.rstrip())
        lineage = taxid.lineage_name(t)
        print(lineage)
    except:
        print("[NA]")
