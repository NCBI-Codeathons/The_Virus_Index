create table viasq.combined_known_interactions as
select 
  virus_tax_id,
  virus_name,
  virus_query_name,
  virus_lineage,
  cast(host_tax_id as INT64) as host_tax_id,
  host_name,
  host_lineage,
  evidence
from viasq.combined_known_interactions_raw
