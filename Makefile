# Makefile for running test scripts
# Author: Christiam Camacho (christiam.camacho@gmail.com)
# Created: Tue Nov  5 12:10:16 EST 2019

SHELL=/bin/bash
.PHONY: all clean distclean check
VPATH=data
VENV=.env

export TAXADB_CONFIG=${PWD}/etc/taxadb.cfg

.PHONY: taxid2lineage
taxid2lineage: init_taxadb
	echo "YES"

# Test code
check: check_python ${VENV}
	[ -f taxadb.sqlite ] || make init_taxadb
	source ${VENV}/bin/activate && echo 9606 | ./taxid2lineage.py
	source ${VENV}/bin/activate && echo "Homo sapiens" | ./name2taxid.py
	source ${VENV}/bin/activate && echo "Mus musculus" | ./name2taxid.py

.PHONY: init_taxadb
init_taxadb: ${VENV}
	source ${VENV}/bin/activate && \
		taxadb download -t taxa -o taxadb && \
		taxadb create -c 200 -d taxa -i taxadb --dbname taxadb.sqlite && \
		${RM} -r taxadb

check_python: ${VENV}
	source ${VENV}/bin/activate && \
	for f in $(wildcard *.py); do python -m py_compile $$f ; done 
	#python3 -m unittest $(subst .py,,$(filter-out setup.py, $(wildcard *.py)))
	#python3 -m unittest discover -s tests
	#time -p python3 -m doctest map.py
	#time -p py.test *.py
	#time -p py.test tests

${VENV}: requirements.txt
	[ -d ${VENV} ] || virtualenv -p python3 $@
	source ${VENV}/bin/activate && pip install -r $^

clean:
	$(RM) -r *.log *.pyc 
	find . -name __pycache__ | xargs ${RM} -fr

distclean: clean
	${RM} -r ${VENV} taxadb*
