#!/usr/bin/env python3
"""
python/sample-viral-index-access.py - See DESC constant below

Author: Christiam Camacho (christiam.camacho@gmail.com)
Created: Wed Nov  6 10:59:55 2019
"""
import os
from viral_index.client import ViralIndex


def main():
    """ Entry point into this program. """
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        print("Please set the GOOGLE_APPLICATION_CREDENTIALS environment variable", file=sys.stderr)
        return 1

    viral_client = ViralIndex()
    cdd_id = 165276
    print('For CDD ID ' + str(cdd_id) + ' here are the SRA runs where it is found')
    runs = viral_client.get_SRAs_where_CDD_is_found(cdd_id)
    if runs is not None:
        for r in runs:
            print(r)

##    print("For CDD ID {}, here are the potential hosts that can be infected by viruses that contain that domain".format(cdd_id))
##    hosts = viral_client.get_hosts_for_virus_domain(cdd_id)
##    if hosts is not None:
##        for h in hosts:
##            print(h)
##

    pig_taxid = 9823
    print("List of viruses that can infect my favorite taxid (Sus scrofa pig): " + str(pig_taxid))
    viruses = viral_client.get_viruses_for_host_taxonomy(pig_taxid)
    if viruses is not None:
        for virus in viruses:
            print(virus)


    HCMV_taxid = 10359
    print("List of hosts that can be infected by my favourite virus (Human cytomegalovirus): " + str(HCMV_taxid))
    hosts_virus = viral_client.get_host_from_virus_taxonomy(HCMV_taxid)
    if hosts_virus is not None:
        for host in hosts_virus:
            print(host)

    # Combining data
    cdd_id = 164925
    print("For CDD ID " + str(cdd_id) + " these are the potential hosts that viruses containing that domain can infect")
    virus_taxids = viral_client.get_potential_hosts_for_virus_domain(cdd_id)
    if virus_taxids is not None:
        for vtaxid in virus_taxids:
            hosts = viral_client.get_host_from_virus_taxonomy(vtaxid)
            if len(hosts) != 0:
                print(hosts)


    evidence = "\'NCBI\'"
    print("List all virus:host interactions based on level of evidence: " + str(evidence))
    evidence_interaction = viral_client.get_virus_host_interactions_from_confidence_level(evidence)
    if evidence_interaction is not None:
        for evi_int in evidence_interaction:
            #print(evi_int)
            print("List it's too long!")

    #interacting with spacerdb
    spacer_seqs=viral_client.get_spacer_seqs(1915496)
    print([s for s in spacer_seqs])

    spacer_seq='CACGAGTGCGAAGCATCCAATCCATATGACTACAT'
    #print(str(spacer_seq))
    spacer_tax_ids=viral_client.get_taxid_from_spacer_seq(str(spacer_seq))
    print([t for t in spacer_tax_ids])



    return 0

if __name__ == "__main__":
    import sys, traceback
    try:
        sys.exit(main())
    except Exception as e:
        print(e, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
