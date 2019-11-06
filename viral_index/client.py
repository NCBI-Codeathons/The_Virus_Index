#!/usr/bin/env python3
# ===========================================================================
#
#                            PUBLIC DOMAIN NOTICE
#               National Center for Biotechnology Information
#
#  This software/database is a "United States Government Work" under the
#  terms of the United States Copyright Act.  It was written as part of
#  the author's official duties as a United States Government employee and
#  thus cannot be copyrighted.  This software/database is freely available
#  to the public for use. The National Library of Medicine and the U.S.
#  Government have not placed any restriction on its use or reproduction.
#
#  Although all reasonable efforts have been taken to ensure the accuracy
#  and reliability of the software and data, the NLM and the U.S.
#  Government do not and cannot warrant the performance or results that
#  may be obtained by using this software or data. The NLM and the U.S.
#  Government disclaim all warranties, express or implied, including
#  warranties of performance, merchantability or fitness for any particular
#  purpose.
#
#  Please cite the author in any work or product based on this material.
#
# ===========================================================================
#
# Author: Christiam Camacho (camacho@ncbi.nlm.nih.gov)
#

from google.auth import compute_engine
from google.cloud import bigquery


class ViralIndex:

    def __init__(self):
        credentials = compute_engine.Credentials()
        self.bq = bigquery.Client(credentials=credentials)


    def get_viruses_for_host_taxonomy(self, taxid):
        """ 
        input: taxonomy ID for the host (integer)
        output: virus_name (list of strings)
        """
        return []

    def get_host_from_virus_taxonomy(self, virus_taxid):
        """
        description: Gets the hosts that can be infected for a given virus taxonomy ID
        input: virus taxonomy ID (integer)
        output: list of possible host_name (list of strings)
        """

    def get_virus_host_interactions_from_confidence_level(self, confidence_level):
        """
        description: Gets the virus-host interactions for given confidence level
        input: confidence_level
        output: virus_taxid, host_taxid
        """

    def get_SRAs_where_CDD_is_found(self, cdd_id_integer):
        """
        input: CDD ID (String) - only viral ones for now.
        output: SRA ID (list of strings)
        """
        query = "select srr from viasq.cdd_data_original where cast(substr(cdd,5) as int64) =  " + str(cdd_id_integer)
        query_job = self.bq.query(query, location="US")

        retval = []
        for row in query_job:  # API request - fetches results
            # Row values can be accessed by field name or index
            retval.append(row[0])
        return retval

    def get_domains(self, virus_taxid):
        """
        input: virus_taxid
        output: HMM domains, score, possibly, from David's group: CDDs, locations?
        """

    def virus_graph(self, virus_taxid):
        """
        input: virus_taxonomy_id
        output: if exists, a VCF file that represents the graph
        """
    def get_spacer_seqs(self, spacer_seq):
        """
        input: taxonomy_id
        output: spacer_seq
        """
    def get_taxid_from_spacer_seq(self, taxid):
        """
        input: spacer_seq
        output: taxonomy_id
        """
