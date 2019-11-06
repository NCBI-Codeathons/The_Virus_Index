#!/bin/bash
set -e

bq --location=US query --use_legacy_sql=false $(cat ./cdd_data_original-augment.sql)
bq --location=US rm -f viasq.cdd_data_original
bq --location=US cp viasq.cdd_data_original_aug viasq.cdd_data_original
bq --location=US rm -f viasq.cdd_data_original_aug
