#!/usr/bin/env python3
from taxadb.names import SciName
import fileinput
names = SciName()
for line in fileinput.input():
    print(names.taxid(line.rstrip()))
