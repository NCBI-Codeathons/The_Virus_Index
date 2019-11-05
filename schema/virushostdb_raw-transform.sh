#!/bin/bash
bq --location=US query --use_legacy_sql=false $(cat ./virushostdb_raw-transform.sql)