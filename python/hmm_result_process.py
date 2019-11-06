import sys

infile = sys.argv[1]

inlines = open(infile, 'r').readlines()

for inline in inlines:
    if inline.startswith('#'):
        continue

    values = inline.strip().split()
    outline = values[0]

    for value in values[1:16]:
        outline = outline + '\t' + value

    for value in values[17:]:
        outline = outline + ' ' + value

    print(outline)
