create table viasq.cdd_data_original_aug as
select 
  contig_id,
  cdd,
  pident,
  length,
  mismatch,
  gapopen,
  qstart,
  qend,
  sstart,
  send,
  evalue,
  bitscore,
  srr,
  concat(srr, '_', contig_id) as sample_contig
from viasq.cdd_data_original
