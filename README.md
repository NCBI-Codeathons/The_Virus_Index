# The_Virus_Index
A Federated Index of Virus Metadata and Hyperdata in Public Repositories

## API
Status: Extensible DRAFT API

[![Build Status](https://travis-ci.com/NCBI-Codeathons/The_Virus_Index.svg?branch=master)](https://travis-ci.com/NCBI-Codeathons/The_Virus_Index)

https://test.pypi.org/project/viral-index/

**Requirements:**
* `python3`
* A Google Cloud Platform (GCP) account. Please see [GCP's getting started guide](https://cloud.google.com/start) if you are new to GCP.

### Developer instructions 

1. Install the `viral-index` module
```bash
python3 -m venv .env
source .env/bin/activate
pip install -q --extra-index-url https://test.pypi.org/simple/ viral-index 
```

2. Configure BigQuery access credentials

Usage of this API requires access to GCP BigQuery. To set up authentication, please follow the instructions in the [section "Setting up authentication" in this page](https://cloud.google.com/bigquery/docs/reference/libraries#setting_up_authentication). **Note**: when prompted to save the JSON file with your key downloads, we suggest we save it to a filename _without_ spaces. In that way it's easier to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable :)

**N.B.**: You _may_ be charged for using this API. Please learn more about [BigQuery pricing](https://cloud.google.com/bigquery/pricing#free-tier).

3. Write your code to access the index!

### Sample code

```python
>>> from viral_index.client import ViralIndex
>>> viral_client = ViralIndex()
>>> cdd_id = 165276
>>> runs = viral_client.get_SRAs_where_CDD_is_found(cdd_id)
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

Additional sample code can be found in [python/sample-viral-index-access.py](python/sample-viral-index-access.py).

### Troubleshooting

1. If you get an error like the one below, it's likely that you don't have
   Bigquery configured properly for your project. See step 2 in developer
   instructions above.

   ```bash
   Access Denied: Project {YOUR_PROJECT_HERE}:
   User does not have bigquery.jobs.create permission in project
   {YOUR_PROJECT_HERE}
   ```

### Maintainer instructions 

#### Maintainer dependencies
1. `make`: Run `sudo apt-get -y -m update && sudo apt-get install -y make` or
   equivalent command for your system.
1. `python3`
1. [GCP SDK](https://cloud.google.com/sdk/)

#### Instructions
1. Check out the source code: `git clone https://github.com/NCBI-Codeathons/The_Virus_Index.git`
1. Set up the python virtual environment: `make .env`
1. Enable python virtualenv: `source .env/bin/activate`
1. Set up the GCP credentials: `export GOOGLE_APPLICATION_CREDENTIALS=${PATH_TO_CREDENTIALS_JSON_FILE}`.
1. Write code that uses `viral_index.client.ViralIndex`

Automated testing is available in [TravisCI](https://travis-ci.com/NCBI-Codeathons/The_Virus_Index).

The `Makefile` has several targets that may be helpful:

* `.env`: initializes the python virtual environment.
* `check_bq`: checks command line access to BigQuery (tool availability and authentication).
* `check_python_syntax`: checks the syntax of python scripts in this repo.
* `check_taxadb`: checks that taxadb was properly installed.
* `check_api`: checks that the API can be retrieved from PyPI, runs demo script.
* `init_taxadb`: Initializes and configures taxadb (needed for the taxonomy utilities).
* `deploy`: Builds a tarball for distribution and uploads it to test.pypi.org (requires `twine`, contact @christiam).
* `setup_bigquery_authentication`: Sample command lines to set up authentication for BigQuery.

The module's version is stored in [setup.py](./setup.py).

## Bonus: Taxonomy utilities

### Dependencies
* [taxadb python module](https://github.com/HadrienG/taxadb)

### Initialize taxadb and environment
(Assumes bash and linux)

1. Download and set up taxadb: Run `make init_taxadb` (this will take about
   2-3 minutes).
2. Initialize python virtual environment: Run `source .env/bin/activate`
3. Set environment variable: `export TAXADB_CONFIG=${PWD}/etc/taxadb.cfg`

### Available tools
* `python/name2taxid.py`: takes scientific names on standard input or input files (spelling is significant) and
  outputs NCBI taxonomy IDs.
* `python/taxid2lineage.py`: takes NCBI taxonomy IDs on standard input (or
  input files) and outputs the lineage for that given taxid. 
  
## Future work
* Review data in BigQuery and integrate it better with the API
