#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Wed 2 Dec 15:43:22 CEST 2015

"""
  ASVspoof database implementation of bob.db.verification.utils.Database interface.
  It is an extension of an SQL-based database interface, which directly talks to ASVspoof database, for
  verification experiments (good to use in bob.bio.base framework).
"""

from . import __doc__ as long_description
from .query import Database as ASVspoofDatabase
from .query import File as ASVspoofFile
import bob.db.verification.utils


class File(bob.db.verification.utils.File):

    def __init__(self, f):
        """
        Initializes this File object with an File equivalent from the underlying SQl-based interface for
        ASVspoof database.
        """
        bob.db.verification.utils.File.__init__(self, client_id=f.client_id, path=f.path, file_id=f.id)

        self.__f = f

    def load(self, directory=None, extension='.hdf5'):
        return self.__f.load(directory=directory, extension=extension)

    load.__doc__ = ASVspoofFile.load.__doc__

    def get_client_id(self):
        """
        Get ID of the client that this file belongs to.
        """

        return self.__f.client_id


class Database(bob.db.verification.utils.Database):
    """
    Implements verification API for querying ASVspoof database.
    """
    __doc__ = long_description

    def __init__(self, original_directory=None, original_extension=None):
        # call base class constructors to open a session to the database
        bob.db.verification.utils.Database.__init__(self, original_directory=original_directory,
                                                    original_extension=original_extension)

        self.__db = ASVspoofDatabase()

    def groups(self, protocol=None):
        """Returns the names of all registered groups"""

        return self.__db.groups()

    def genders(self):
        """Returns the list of genders"""

        return self.__db.genders()

    def protocols(self):
        """Returns all registered protocols"""
        return self.__db.protocols()

    def protocol_names(self):
        """Returns all registered protocol names"""

        return self.__db.protocol_names()

    def has_protocol(self, name):
        """Tells if a certain protocol is available"""

        return self.__db.has_protocol(name)

    def protocol(self, name):
        """Returns the protocol object in the database given a certain name. Raises
        an error if that does not exist."""

        return self.__db.protocol(name)

    def models(self, groups=None, protocol=None, gender=None):
        """Returns a set of models for the specific query by the user.

        Keyword Parameters:

        protocol
            Protocol is ignored in this context, since its choice has no influence on models.

        groups
            The groups to which the subjects attached to the models belong ('dev', 'eval', 'world')

        gender
            The gender to consider ('male', 'female')

        Returns: A list containing the ids of all models belonging to the given group.
        """
        return self.__db.clients(groups=self._convert_group_names(groups), gender=gender)

    def model_ids(self, groups=None, protocol=None, gender=None):
        """Returns a set of models ids for the specific query by the user.

        Keyword Parameters:

        protocol
            Protocol is ignored in this context, since its choice has no influence on models.

        groups
            The groups to which the subjects attached to the models belong ('dev', 'eval', 'world')

        gender
            The gender to consider ('male', 'female')

        Returns: A list containing the ids of all models belonging to the given group.
        """
        return [client.id for client in self.__db.clients(groups=self._convert_group_names(groups), gender=gender)]

    def clients(self, protocol=None, groups=None, gender=None):
        """Returns a list of Clients for the specific query by the user.
           If no parameters are specified - return all clients.

        Keyword Parameters:

        protocol
            Protocol is ignored in this context, since its choice has no influence on clients.

        groups
            The groups to which the subjects attached to the models belong ('dev', 'eval', 'world')

        gender
            The gender to consider ('male', 'female')

        Returns: A list containing the ids of all models belonging to the given group.
        """

        return self.__db.clients(groups=self._convert_group_names(groups), gender=gender)

    def has_client_id(self, id):
        """Returns True if we have a client with a certain integer identifier"""

        return self.__db.has_client_id(id)

    def client(self, id):
        """Returns the Client object in the database given a certain id. Raises
        an error if that does not exist."""

        return self.__db.client(id)

    def get_client_id_from_model_id(self, model_id, **kwargs):
        """Returns the client_id attached to the given model_id

        Keyword Parameters:

        model_id
            The model_id to consider

        Returns: The client_id attached to the given model_id
        """
        return model_id

    def annotations(self, file):
        """Currently, there is no support for annotations in ASVspoof database
        """
        return None

    def _convert_group_names(self, groups):
        """ convert verification groups to what is used in __db
        """
        if groups is None:
            return None
        group_alias = {'world': 'train', 'dev': 'dev', 'eval': 'eval'}
        matched_groups = []
        if isinstance(groups, (tuple, list)):
            for group in groups:
                matched_groups += [group_alias[group]]
        else:
            matched_groups = [group_alias[groups]]
        return matched_groups

    def objects(self, protocol=None, purposes=None, model_ids=None,
                groups=None, gender=None):
        """Returns a set of Files for the specific query by the user.

        Keyword Parameters:

        protocol
            Each valid protocol of the AVspoof database can have a '-licit' or '-spoof' appended to it.
            If the '-licit' is appended, then the only real or genuine data of the protocol will be used.
            If '-spoof' is appended, then attacks or spoofed data will be used as the probe set.
            If nothing is appended, then 'licit' option is assumed by default.

        purposes
            The purposes can be either 'enroll', 'probe', or their tuple.
            If 'None' is given (this is the default), it is
            considered the same as a tuple with both possible values.

        model_ids
            Only retrieves the files for the provided list of model ids (claimed
            client id).  If 'None' is given (this is the default), no filter over
            the model_ids is performed.

        groups
            One of the groups ('dev', 'eval', 'world') or a tuple with several of them.
            If 'None' is given (this is the default), it is considered the same as a
            tuple with all possible values.

        gender
            The gender to consider ('male', 'female')

        Returns: A set of Files with the specified properties.
        """

        # convert group names from the conventional in verification experiments to the internal database names
        matched_groups = self._convert_group_names(groups)

        # this conversion of the protocol with appended '-licit' or '-spoof' is a hack for verification experiments.
        # To adapt spoofing databases to the verification experiments, we need to be able to split a given protocol
        # into two parts: when data for licit (only real/genuine data is used) and data for spoof (attacks are used instead
        # of real data) is used in the experiment. Hence, we use this trick with appending '-licit' or '-spoof' to the
        # protocol name, so we can distinguish these two scenarios.
        # By default, if nothing is appended, we assume licit protocol.
        # The distinction between licit and spoof is expressed via purposes parameters
        # this is the difference in terminology.

        # lets check if we have an appendix to the protocol name
        appendix = None
        if protocol:
            appendix = protocol.split('-')[-1]

        # if protocol was empty or there was no correct appendix, we just assume the 'licit' option
        if not (appendix == 'licit' or appendix == 'spoof'):
            appendix = 'licit'
        else:
            # put back everything except the appendix into the protocol
            protocol = '-'.join(protocol.split('-')[:-1])

        # if protocol was empty, we set it to the grandtest, which is the whole data
        if not protocol:
            protocol = 'CM'

        correct_purposes = purposes
        # licit protocol is for real access data only
        if appendix == 'licit':
            # by default we assume all real data
            if purposes is None:
                correct_purposes = ('real', 'impostor')

        # for any other protocol use real data and spoofed data (probe)
        # so, probe set is the same as attack set
        else:
            # by default we return all data (enroll:realdata + probe:attackdata)
            if purposes is None:
                correct_purposes = ('real', 'attack')
            # otherwise replace 'probe' with 'attack'
            elif isinstance(purposes, (tuple, list)):
                correct_purposes = []
                for purpose in purposes:
                    if purpose == 'probe':
                        correct_purposes += ['attack']
                    else:
                        correct_purposes += [purpose]
            elif purposes == 'probe':
                correct_purposes = ('attack',)

        # now, query the actual ASVspoof database
        if 'attack' in correct_purposes:
            objects = self.__db.objects(protocol=protocol, groups=matched_groups, purposes=correct_purposes,
                                        clients=model_ids, gender=gender)
        else:
            objects = self.__db.objects(protocol=protocol, groups=matched_groups, purposes=correct_purposes,
                                        clients=model_ids, gender=gender)
        # make sure to return verification.utils representation of a file, not the database one
        return [File(f) for f in objects]
