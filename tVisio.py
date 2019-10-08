import sys
import os
import logging
import logging.config
import copy
import types

import json
import requests

# import settings

__version__ = "1.0"


def _showAll(args):
    all = copy.copy(args.items())
    print "Script version", __version__

    for name, f in all:
        if isinstance(f, types.FunctionType):
            if not name.startswith("_"):
                print "******************************"
                print "Function ** %s **" % name
                print "******************************"
                if f.__doc__ is not None:
                    print '\t', f.__doc__


def t1(args):
    from requests.utils import quote
    from lxml import html
    from lxml import etree

    from bs4 import BeautifulSoup

    fn = args[0]
    print 'Reading {}'.format(fn)

    with open(fn, "r") as fp:
        soup = BeautifulSoup(fp, features="xml")

        allText = soup.find_all("Text")
        for t in allText:
            print t.text.strip()


if __name__ == '__main__':
    REVISION = "$LastChangedRevision: 10220 $"
    if os.path.exists("logging.conf"):
        logging.config.fileConfig("logging.conf")
        logging.info("Using logging.conf for logging settings.")
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info('Version =%s', REVISION)
    if len(sys.argv) < 2:
        _showAll(locals())
        os._exit(0)

    # Globals
    fnName = sys.argv[1]
    logging.info('Function *** %s ***', fnName)

    if fnName not in locals():
        logging.error("Unknown function '%s'", fnName)
        os._exit(0)

    n = locals()[fnName](args=sys.argv[2:])
    sys.stdout.flush()

    logging.info('** bye')
    os._exit(0)
