#!/bin/bash
bq --location=US load --source_format=CSV --replace=true --field_delimiter="," --allow_jagged_rows --allow_quoted_newlines viasq.accessions2species_raw gs://virus-hunting-2-codeathon-viasq-team/accessions2species_raw.csv ./accessions2species_raw-schema.json