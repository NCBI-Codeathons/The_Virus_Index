#!/bin/bash
bq --location=US load --source_format=CSV --replace=true --field_delimiter="\t" datasource.sampletable gs://bucket/sampletable/*.csv ./sampletable_schema.json
