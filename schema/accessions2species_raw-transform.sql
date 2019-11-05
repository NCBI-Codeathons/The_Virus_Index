create table viasq.accessions2species as
select 
if (accession = '', NULL, accession) as accession,
if (species = '', NULL, species) as species
from viasq.accessions2species_raw
