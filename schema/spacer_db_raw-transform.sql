create table viasq.spacer_db as
select 
  taxonomy_gtdb,
  accession,
  array_id,
  spacer_id,
  spacer_seq,
  accession3,
  source,
  if (ncbi_tax_id in ('none', 'NA'), NULL, cast(ncbi_tax_id as INT64)) as ncbi_tax_id
from viasq.spacer_db_raw
