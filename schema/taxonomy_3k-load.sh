#!/bin/bash
bq --location=US load --skip_leading_rows=1 --source_format=CSV --replace=true --field_delimiter="\t" --allow_jagged_rows --allow_quoted_newlines viasq.taxonomy_3k gs://virus-hunting-2-codeathon-viasq-team/Taxonomy_Domain_Integration/taxonomy_3k.tsv ./taxonomy_3k-schema.json
