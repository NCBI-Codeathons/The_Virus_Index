# The_Virus_Index
A Federated Index of Virus Metadata and Hyperdata in Public Repositories

## API
Status: Extensible DRAFT

[![Build Status](https://travis-ci.com/NCBI-Codeathons/The_Virus_Index.svg?branch=master)](https://travis-ci.com/NCBI-Codeathons/The_Virus_Index)

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

>>> pig_taxid = 9823
>>> viruses = viral_client.get_viruses_for_host_taxonomy(pig_taxid)
>>> if viruses is not None:
        for virus in viruses:
            print(virus)
['Rotavirus C', 36427]
['Porcine rubulavirus', 53179]
['Porcine associated porprismacovirus 7', 2170123]
['Porcine enterovirus b/BEL/15V010', 2017720]
[...]
>>>

>>> spacer_seqs=viral_client.get_spacer_seqs(1915496)
>>> print([s for s in spacer_seqs])
[['112', 'CAGCCATCCGCGACGCCACGACAGCGGCCGAGAGTGT', 'GCF_002508705', 'GTDB'], ['1', 'AATCAGCCCGTCGGGGTAGCCAGGGACGCCCTCCA', 'GCF_002508705', 'GTDB'],
[...]

>>> spacer_seq='CACGAGTGCGAAGCATCCAATCCATATGACTACAT'
>>> spacer_tax_ids=viral_client.get_taxid_from_spacer_seq(str(spacer_seq))
>>> print([t for t in spacer_tax_ids])
[['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915496], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915507], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915502], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915504], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915506], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915510], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915499], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915512], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915500], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915495], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915498], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915505], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915508], ['31', 'CACGAGTGCGAAGCATCCAATCCATATGACTACAT', 'GCF_002508705', 'GTDB', 1915503]]
```

## Taxonomy utilities

### Dependencies
* taxadb python module: https://github.com/HadrienG/taxadb

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
