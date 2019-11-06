create table viasq.known_interactions_db as
select 
  virus_tax_id,
  virus_name,
  virus_lineage,
  cast(host_tax_id as INT64) as host_tax_id,
  host_name,
  host_lineage,
  evidence
from viasq.known_interactions_db_raw
