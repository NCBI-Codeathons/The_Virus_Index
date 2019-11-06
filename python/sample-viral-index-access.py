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
    runs = viral_client.get_SRAs_where_CDD_is_found(165276)
    for r in runs:
        print(r)
    return 0


if __name__ == "__main__":
    import sys, traceback
    try:
        sys.exit(main())
    except Exception as e:
        print(e, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

