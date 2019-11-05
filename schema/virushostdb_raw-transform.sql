create table viasq.virushostdb as
select 
if (virus_taxid = '', NULL, cast(virus_taxid as int64)) as virus_taxid,
if (virus_name = '', NULL, virus_name) as virus_name,
if (virus_lineage = '', NULL, virus_lineage) as virus_lineage,
if (refseq_id = '', NULL, refseq_id) as refseq_id,
if (kegg_genome = '', NULL, kegg_genome) as kegg_genome,
if (kegg_disease = '', NULL, kegg_disease) as kegg_disease,
if (disease = '', NULL, disease) as disease,
if (host_taxid = '', NULL, cast(host_taxid as int64)) as host_taxid,
if (host_name = '', NULL, host_name) as host_name,
if (host_lineage = '', NULL, host_lineage) as host_lineage,
if (pmid = '', NULL, pmid) as pmid,
if (evidence = '', NULL, evidence) as evidence,
if (sample_type = '', NULL, sample_type) as sample_type,
if (source_organism = '', NULL, source_organism) as source_organism
from viasq.virushostdb_raw
