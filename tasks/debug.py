#! /home/thom/ve/2.7/bin/python
from __future__ import unicode_literals
import sys

from logbook import Logger

from uscode import File
from utils import title_filename


logger = Logger('debug')


def run(options):
    filename = title_filename(int(options["title"]), '2011')
    fp = open(filename)

    gpo_file = File(fp)
    succeeded = 0
    failed = 0
    for section in gpo_file.sections():
        logger.info('Trying to parse %r' % section)
        try:
            tree = section.as_tree()
        except Exception as e:
            logger.warning('  .. parse failed: %r' % e)
            failed += 1
        else:
            succeeded += 1

    logger.info('Number that succeeded: %d' % succeeded)
    logger.info('Number that failed: %d' % failed)
    logger.info('Percent success: %f' % (1 - (1.0 * failed / succeeded)))





    # ss = ff[int(options["offset"])].instance
    # bb = ss.body_lines()
    # xx = GPOLocatorParser(bb)
    # qq = xx.parse()
    # qq.tree()
    # js = qq.json()

    import pdb;pdb.set_trace()

    # xx = [x.instance for x in gg]

    # import pdb;pdb.set_trace()
    # for doc in gg:
    #     x = doc.instance
    #     print x
    #     import pdb;pdb.set_trace()


if __name__ == '__main__':
    run()
