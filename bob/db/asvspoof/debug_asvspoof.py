#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Wed 19 Aug 13:43:50 2015
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
