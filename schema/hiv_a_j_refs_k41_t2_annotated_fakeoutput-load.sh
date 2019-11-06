#!/bin/bash
bq --location=US load --skip_leading_rows=1 --source_format=CSV --replace=true --field_delimiter="\t" --allow_jagged_rows --allow_quoted_newlines viasq.hiv_a_j_refs_k41_t2_annotated_fakeoutput gs://virus-hunting-2-codeathon-viasq-team/VirGraph/HIV_A-J_Refs_k41_t2_annotated.fakeOutput.tsv ./hiv_a_j_refs_k41_t2_annotated_fakeoutput-schema.json
