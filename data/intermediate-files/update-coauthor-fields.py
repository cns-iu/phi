#!/usr/bin/env python3
import csv, os.path

DATA_DIR=os.path.dirname(os.path.abspath(__file__))
MAPPINGS=os.path.join(DATA_DIR, 'wos-extract.cleaned-coauthornet.csv')
ORIGINAL=os.path.join(DATA_DIR, 'wos-extract.csv')
OUT=os.path.join(DATA_DIR, 'wos-extract.cleaned-coauthornet.for-sci2.csv')
SKIP_UNMAPPED_PUBS = True
MAX_AUTHORS_PER_PUB = 100

mappings = {}
with open(MAPPINGS) as m_in:
  for row in csv.DictReader(m_in):
    mappings[row['id']] = row

with open(ORIGINAL) as o_in, open(OUT, 'w') as out_f:
  writer = csv.writer(out_f)
  header = False
  remaps = 0
  for row in csv.reader(o_in):
    if not header:
      header = dict( (field, i) for (i, field) in enumerate(row) )
    else:
      uid = row[header['Unique ID']]

      if uid in mappings and len(mappings[uid]['name-revised'].split('|')) >= MAX_AUTHORS_PER_PUB:
        print(uid, len(mappings[uid]['name-revised'].split('|')))

      if uid in mappings and len(mappings[uid]['name-revised'].split('|')) < MAX_AUTHORS_PER_PUB:
        remaps += 1
        row[header['Authors']] = '|'.join(set(mappings[uid]['name-revised'].split('|')))
        row[header['Authors (Full Names)']] = mappings[uid]['fullname-revised']
      elif SKIP_UNMAPPED_PUBS:
        continue

    writer.writerow(row)

  print(f'Remapped {remaps} rows')
