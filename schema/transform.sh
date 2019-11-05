#!/bin/bash
tablename=$1
bq --location=US query --use_legacy_sql=false $(cat ./${tablename}-transform.sql)