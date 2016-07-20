#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Wed 19 Aug 13:43:50 2015
#


"""A few checks at the asvspoof attack database.
"""

from __future__ import print_function

from .query import Database
from .models import *


def db_available(test):
    """Decorator for detecting if OpenCV/Python bindings are available"""
    from bob.io.base.test_utils import datafile
    from nose.plugins.skip import SkipTest
    import functools

    @functools.wraps(test)
    def wrapper(*args, **kwargs):
        dbfile = datafile("db.sql3", __name__, None)
        if os.path.exists(dbfile):
            return test(*args, **kwargs)
        else:
            raise SkipTest(
                "The database file '%s' is not available; did you forget to run 'bob_dbmanage.py %s create' ?" % (
                dbfile, 'asvspoof'))

    return wrapper


# class ASVspoofDatabaseTest(unittest.TestCase):
class ASVspoofDatabaseTest():
    """Performs various tests on the asvspoof attack database."""

    @db_available
    def test01_queryDatabase(self):
        db = Database()
        f = db.objects()
        print ("Objects set is %s" % str(f))



def main():
    test = ASVspoofDatabaseTest()
    test.test01_queryDatabase()


if __name__ == '__main__':
    main()
