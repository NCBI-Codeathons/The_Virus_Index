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

    if len(sys.argv) <= 1:
        print("Please provide a CDD ID integer")
        return 1

    cdd_id = sys.argv[1]
    viral_client = ViralIndex()
    print("For CDD ID " + str(cdd_id) + " these are the potential hosts that viruses containing that domain can infect")
    virus_taxids = viral_client.get_potential_hosts_for_virus_domain(cdd_id)
    if virus_taxids is not None:
        for vtaxid in virus_taxids:
            hosts = viral_client.get_host_from_virus_taxonomy(vtaxid)
            if len(hosts) != 0:
                print(hosts)

    return 0


if __name__ == "__main__":
    import sys, traceback
    try:
        sys.exit(main())
    except Exception as e:
        print(e, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

