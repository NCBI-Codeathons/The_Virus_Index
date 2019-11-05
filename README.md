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
There is no fixed taxonomica level for viral graphs (ie within genus, within family)


# Presentation 05/11/19

* We're looking for data!
  * Please put in the bucket, see sample commands [here](https://github.com/NCBI-Codeathons/The_Virus_Index/issues/4#issuecomment-549868892)
* Pseudo-code for _eventual_ API:
 * *very early* draft [here](https://github.com/NCBI-Codeathons/The_Virus_Index/issues/5)
* Question: scope of data
 * Some groups are working with SRA contigs from previous hackathons
    * 3000 dataset?
 * Others are working on data from Genbank (i.e.: metadata already provided by
   NCBI Virus webpage). Is there new metadata (that's not offered by NCBI)?
   What's the added value? Is it a subset of the full set?
   E.g.: Host-phage interaction & Domain-HMM groups
 * Integration of SRA data and Genbank data?


* __AWESOME__ progress: Alex loaded Ryan's data (Accession, species) to BigQuery
  
  

