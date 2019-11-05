#!/usr/bin/env python3
from taxadb.taxid import TaxID
import fileinput
taxid = TaxID()
for line in fileinput.input():
    print(taxid.sci_name(line.rstrip()))
