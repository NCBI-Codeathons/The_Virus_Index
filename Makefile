# Makefile for running test scripts
# Author: Christiam Camacho (christiam.camacho@gmail.com)
# Created: Tue Nov  5 12:10:16 EST 2019

SHELL=/bin/bash
.PHONY: all clean distclean check
VENV=.env

export TAXADB_CONFIG=${PWD}/etc/taxadb.cfg
export GOOGLE_APPLICATION_CREDENTIALS=${PWD}/etc/cred.json

########################################################################################
# BigQuery targets
SVC_ACCT_NAME=bg-access-${USER}
GCP_PROJECT_ID?=${USER}

.PHONY: setup_bigquery_authentication
setup_bigquery_authentication:
	echo ${GCP_PROJECT_ID}
	gcloud iam service-accounts create ${SVC_ACCT_NAME}
	gcloud projects add-iam-policy-binding ${GCP_PROJECT_ID} --member "serviceAccount:${SVC_ACCT_NAME}@${GCP_PROJECT_ID}.iam.gserviceaccount.com" --role "roles/owner"
	gcloud iam service-accounts keys create ${GOOGLE_APPLICATION_CREDENTIALS} --iam-account ${SVC_ACCT_NAME}@${GCP_PROJECT_ID}.iam.gserviceaccount.com

.PHONY: check_bq
check_bq:
	bq query --use_legacy_sql=false 'SELECT count(*) FROM `virus-hunting-2-codeathon.viasq.cdd_data`'

########################################################################################
# Test code
check_taxadb: check_python_syntax ${VENV}
	[ -f taxadb.sqlite ] || make init_taxadb
	source ${VENV}/bin/activate && echo 9606 | ./python/taxid2lineage.py
	source ${VENV}/bin/activate && echo None | ./python/taxid2lineage.py
	source ${VENV}/bin/activate && echo 10090 | ./python/taxid2name.py
	source ${VENV}/bin/activate && echo junk | ./python/taxid2name.py
	source ${VENV}/bin/activate && echo "Homo sapiens" | ./python/name2taxid.py
	source ${VENV}/bin/activate && echo "Mus musculus" | ./python/name2taxid.py

check_api: ${VENV} check_python_syntax
	tests/check-module.sh
	source ${VENV}/bin/activate && python/sample-viral-index-access.py

.PHONY: init_taxadb
init_taxadb: ${VENV}
	source ${VENV}/bin/activate && \
		taxadb download -t taxa -o taxadb && \
		taxadb create -c 200 -d taxa -i taxadb --dbname taxadb.sqlite && \
		${RM} -r taxadb

check_python_syntax: ${VENV}
	source ${VENV}/bin/activate && \
		for f in $(wildcard python/*.py); do python -m py_compile $$f ; done

${VENV}: requirements.txt
	[ -d ${VENV} ] || python3 -m venv $@
	source ${VENV}/bin/activate && pip install -r $^
	source ${VENV}/bin/activate && pip install -r requirements/test.txt
	source ${VENV}/bin/activate && pip install -e .

##############################################################################
# pypi support
MODULE_NAME?=viral_index
PYTHON_MODULE_VERSION=$(shell grep version setup.py | cut -d= -f 2 | tr -d \'  | tr -d , )
dist/${MODULE_NAME}-${PYTHON_MODULE_VERSION}.tar.gz:
	python setup.py sdist

# twine --repository assumes ~/.pypirc settings include username/password; --repository-url prompts them
TEST_PYPI=https://test.pypi.org
.PHONY: deploy
deploy: dist/${MODULE_NAME}-${PYTHON_MODULE_VERSION}.tar.gz
	#source ${VENV}/bin/activate && twine upload --repository-url ${TEST_PYPI}/legacy/ $<
	source ${VENV}/bin/activate && twine upload --repository testpypi $<
	#source ${VENV}/bin/activate && twine upload $<


clean:
	$(RM) -r *.log *.egg-info dist
	find . -name __pycache__ | xargs ${RM} -fr
	find . -name '*.pyc' | xargs ${RM} -fr

distclean: clean
	${RM} -r ${VENV} taxadb*
