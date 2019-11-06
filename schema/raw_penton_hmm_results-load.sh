#!/bin/bash
bq --location=US load --source_format=CSV --replace=true --field_delimiter="\t" --allow_jagged_rows --allow_quoted_newlines viasq.raw_penton_hmm_results gs://virus-hunting-2-codeathon-viasq-team/Taxonomy_Domain_Integration/raw_penton_hmm_results_transformed.tsv ./raw_penton_hmm_results-schema.json
