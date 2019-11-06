# The_Virus_Index
A Federated Index of Virus Metadata and Hyperdata in Public Repositories


# What we'd like to do?
* Collaborate with other teams to define a data model
  * Give us your use case!
* Put the data on a cloud resource (BigQuery)
  * Ideas for features
     * Biome
     * Domains 
     * Geographical location
     * Is there hierarchical data?
     * Temporal data
     * Data already in SRA: Taxonomy?
     
* Provide convenient access to this data (i.e.: not for programmers only). 
  * Possible examples: 
    * [NCBI virus webpage](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) [old page](https://www.ncbi.nlm.nih.gov/genome/viruses/)
    * [EBI Virus page](https://www.ebi.ac.uk/genomes/virus.html)
    
  * Get data into [pandas](https://pandas.pydata.org/)?
  * How would researchers like to access this data (from which purview)? Genomic context?
    * Complete genomes, specific genes (philogenetic markers). 
    * Contig based?
  
  
  # Flow chart
See ![Virus Indexing and Sequence Quality Team Scope.pdf](
https://github.com/NCBI-Codeathons/The_Virus_Index/raw/master/Virus%20Indexing%20and%20Sequence%20Quality%20Team%20Scope.pdf)


Notes from other teams: 
A particular virus (entry in the db) can belong to multiple viral graphs.

There is no fixed taxonomica level for viral graphs (ie within genus, within family).


# Presentation 11/05/19

* We're looking for data!
  * Please put in the bucket, see sample commands [here](https://github.com/NCBI-Codeathons/The_Virus_Index/issues/4#issuecomment-549868892)
* Pseudo-code for _eventual_ API:
    * *very early* draft [here](https://github.com/NCBI-Codeathons/The_Virus_Index/issues/5)
* Question: Scope of data
 * Some groups are working with SRA contigs from previous hackathons
    * 3000 dataset?
    * Is it worth the pain of deconvoluting what we did for this one?
 * Others are working on data from Genbank (i.e.: metadata already provided by
   NCBI Virus webpage). Is there new metadata (that's not offered by NCBI)?
   What's the added value? Is it a subset of the full set?
   E.g.: Host-phage interaction & Domain-HMM groups
 * Integration of SRA data and Genbank data?
 * Is anybody working with ENA data?


* __AWESOME__ progress: Alex loaded Ryan's data (Accession, species) to BigQuery
  
  
## API
Status: Extensible DRAFT

[![Build Status](https://travis-ci.org/NCBI-Codeathons/The_Virus_Index.svg?branch=master)](https://travis-ci.org/NCBI-Codeathons/The_Virus_Index)

https://test.pypi.org/project/viral-index/

### Instructions to use

1. Check out the source code: `git clone https://github.com/NCBI-Codeathons/The_Virus_Index.git`
1. Set up the python virtual environment: `make .env`
1. Enable python virtualenv: `source .env/bin/activate`
1. Set up the GCP credentials: `export GOOGLE_APPLICATION_CREDENTIALS=${PATH_TO_CREDENTIALS_JSON_FILE}` - Ask Alex, Christiam or Carl about this.
1. Write code that uses `viral_index.client.ViralIndex`

### Sample code

```python
>>> from viral_index.client import ViralIndex
>>> viral_client = ViralIndex()
>>> runs = viral_client.get_SRAs_where_CDD_is_found(165276)
<generator object <genexpr> at 0x7fc0d9de0eb8>
>>> print([r for r in runs])
['SRR2187433', 'SRR533343', 'ERR1915143']
>>> 
```

## Taxonomy utilities

### Dependencies
* taxadb python module

### Initialize taxadb and environment
(Assumes bash and linux)

1. Download and set up taxadb: Run `make init_taxadb` (this will take about
   2-3 minutes)
2. Initialize python virtual environment: Run `source .env/bin/activate`
3. Set environment variable: `export TAXADB_CONFIG=${PWD}/etc/taxadb.cfg`

### Available tools
* `python/name2taxid.py`: takes scientific names on standard input or input files (spelling is significant) and
  outputs NCBI taxonomy IDs.
* `python/taxid2lineage.py`: takes NCBI taxonomy IDs on standard input (or
  input files) and outputs the lineage for that given taxid. 
