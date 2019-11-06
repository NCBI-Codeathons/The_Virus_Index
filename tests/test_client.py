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

import unittest
from viral_index.client import ViralIndex


class TestViralIndex(unittest.TestCase):

    def setUp(self):
        self.vcli = ViralIndex()

    def test_function_get_host_from_virus_taxonomy(self):
        virus_names = self.vcli.get_host_from_virus_taxonomy(9606)
        self.assertIsNone(virus_names)

    def test_function_get_SRAs_where_CDD_is_found(self):
        sra_runs = self.vcli.get_SRAs_where_CDD_is_found(9606)
        self.assertIsNotNone(sra_runs)
        self.assertTrue(len(sra_runs) > 0)

    def tearDown(self):
        pass
