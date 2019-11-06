#!/bin/bash
bq --location=US load --skip_leading_rows=1 --source_format=CSV --replace=true --field_delimiter="\t" --allow_jagged_rows --allow_quoted_newlines viasq.raw_penton_hmm_results gs://virus-hunting-2-codeathon-viasq-team/Taxonomy_Domain_Integration/raw_penton_hmm_results_table.tsv ./raw_penton_hmm_results-schema.json
