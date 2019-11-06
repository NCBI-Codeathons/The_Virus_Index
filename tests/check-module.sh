#!/bin/bash
# tests/check-module.sh: Script to check the module's deployment to PyPI
#
# Author: Christiam Camacho (christiam.camacho@gmail.com)
# Created: Wed Nov  6 06:57:16 2019

export PATH=/bin:/usr/bin:/usr/local/bin
shopt -s nullglob
set -xeuo pipefail

TMP=`mktemp -d`
trap " /bin/rm -fr $TMP " INT QUIT EXIT HUP KILL ALRM
pushd $TMP

virtualenv -p python3 .env
set +x
source .env/bin/activate
set -x
pip install google-cloud-bigquery
pip install -i https://test.pypi.org/simple/ viral-index
popd
