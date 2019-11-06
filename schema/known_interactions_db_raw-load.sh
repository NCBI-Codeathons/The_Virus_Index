#!/bin/bash
bq --location=US load --skip_leading_rows=1 --source_format=CSV --replace=true --field_delimiter="," --allow_jagged_rows --allow_quoted_newlines viasq.known_interactions_db_raw gs://virus-hunting-2-codeathon-viasq-team/hpi/KnownInteractionsDB.csv ./known_interactions_db_raw-schema.json
