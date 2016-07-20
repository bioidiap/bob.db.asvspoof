#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Wed 2 Dec 14:43:22 2015

"""
  ASVspoof database implementation of antispoofing.utils.db.Database interface. This interface is useful in
  anti-spoofing experiments. It is an extension of an SQL-based interface, which deals
  with ASVspoof database directly.
"""

from .query import Database as ASVspoofDatabase
import antispoofing.utils
import six


class File(antispoofing.utils.db.File):
    def __init__(self, f):
        """
        Initializes this File object with an File equivalent from the underlying SQl-based interface for
        ASVspoof database
        """

        self.__f = f

    # type object 'File' has no attribute 'audiofile'
    def videofile(self, directory=None):
        """
        This method is used to return an audio file (at the moment, ASVspoof contains audio files only).
        We use 'videofile' method here because antispoofing.utils.db.File interface does not define an audiofile,
        which makes things a little ugly.

        :return: Audio file from ASVspoof database.
        """
        return self.__f.audiofile(directory=directory)

    def facefile(self, directory=None):
        """
        A legacy method from antispoofing.utils.db.File interface.
        Since there are no faces in ASVspoof, this method returns None.
        :return: None
        """
        return None

    def bbx(self, directory=None):
        """
        A legacy method from antispoofing.utils.db.File interface.
        Since there are no bounding boxes in ASVspoof, this method returns None.
        :return: None
        """
        return None

    def load(self, directory=None, extension='.hdf5'):
        return self.__f.load(directory=directory, extension=extension)

    load.__doc__ = antispoofing.utils.db.File.load.__doc__

    def save(self, data, directory=None, extension='.hdf5'):
        return self.__f.save(data, directory=directory, extension=extension)

    save.__doc__ = antispoofing.utils.db.File.save.__doc__

    def make_path(self, directory=None, extension=None):
        return self.__f.make_path(directory=directory, extension=extension)

    make_path.__doc__ = antispoofing.utils.db.File.make_path.__doc__

    def get_client_id(self):
        return self.__f.client_id

    get_client_id.__doc__ = antispoofing.utils.db.File.get_client_id.__doc__

    def is_real(self):
        return self.__f.is_real()

    is_real.__doc__ = antispoofing.utils.db.File.is_real.__doc__

    def get_attacktype(self):
        """
        Attack type of this file
        :return: the type of attack (specified in the File of the database Model)
        """
        return self.__f.attacktype

    def get_protocol(self):
        """
        Protocol this file belongs to
        :return: the protocol name
        """
        return self.__f.protocolfiles.protocol.name

class Database(antispoofing.utils.db.Database):
    """ Implements API of antispoofing interface for ASVspoof database"""

    def __init__(self, args=None):
        self.__db = ASVspoofDatabase()

        self.__kwargs = {}

        if args is not None:
            self.__kwargs = {
                'protocol': args.ASVspoof_protocol,
                'support': args.ASVspoof_support,
                'clients': args.ASVspoof_client if args.ASVspoof_client else None,
            }

    __init__.__doc__ = antispoofing.utils.db.Database.__init__.__doc__

    def set_kwargs(self, params):
        """
        Set internal __kwargs variable, since it is used as a filter to retrieve data from the database
        :param params: dictionary of pairs {"param":"value"} that are accepted by the database as filters,
        for instance, it can be "protocol":"specific_protocol_name".
        :return: None
        """
        self.__kwargs.update(params)

    def get_protocols(self):
        return [k.name for k in self.__db.protocols()]

    get_protocols.__doc__ = antispoofing.utils.db.Database.get_protocols.__doc__

    def get_attack_types(self):
        # In the case of this DB, this method does not precisely return the attack types
        return [k.name for k in self.__db.protocols()]

    get_attack_types.__doc__ = antispoofing.utils.db.Database.get_attack_types.__doc__

    def create_subparser(self, subparser, entry_point_name):
        from .models import Client as ASVspoofClientModel, File as ASVspoofFileModel
        from argparse import RawDescriptionHelpFormatter

        ## remove '.. ' lines from rst
        #    desc = '\n'.join([k for k in self.long_description().split('\n') if k.strip().find('.. ') != 0])

        p = subparser.add_parser(entry_point_name,
                                 help=self.short_description(),
                                 description="ASVspoof database",
                                 formatter_class=RawDescriptionHelpFormatter)

        protocols = [k.name for k in self.__db.protocols()]
        p.add_argument('--protocol', type=str, default='CM',
                       choices=protocols, dest="ASVspoof_protocol", nargs='+',
                       help='The protocol type may be specified instead of the the id switch to subselect a smaller number of files to operate on (defaults to "%(default)s")')

        supports = ASVspoofFileModel.attacktype_choices
        p.add_argument('--support', type=str, dest='ASVspoof_support', choices=supports,
                       help="If you would like to select a specific support to be used, use this option (if unset, the default, use all)")

        genders = ASVspoofClientModel.gender_choices
        p.add_argument('--gender', type=str, choices=genders, dest='ASVspoof_devices',
                       help="The gender of clients (if unset, the default, use all)")

        identities = [k.id for k in self.__db.clients()]
        p.add_argument('--client', type=int, action='append', choices=identities, dest='ASVspoof_client',
                       help="Client identifier (if unset, the default, use all)")

        p.set_defaults(name=entry_point_name)
        p.set_defaults(cls=Database)

        return

    create_subparser.__doc__ = antispoofing.utils.db.Database.create_subparser.__doc__

    def name(self):
        from .driver import Interface
        i = Interface()
        return "ASVspoof Database (%s)" % i.name()
    name.__doc__ = antispoofing.utils.db.Database.name.__doc__

    def short_name(self):
        from .driver import Interface
        i = Interface()
        return i.name()

    short_name.__doc__ = antispoofing.utils.db.Database.short_name.__doc__

    def version(self):
        from .driver import Interface
        i = Interface()
        return i.version()

    version.__doc__ = antispoofing.utils.db.Database.version.__doc__

    def short_description(self):
        return "Automatic Speaker Verification Spoofing and Countermeasures Challenge (ASVspoof 2015) Database"

    short_description.__doc__ = antispoofing.utils.db.Database.short_description.__doc__

    def long_description(self):
        return Database.__doc__

    long_description.__doc__ = antispoofing.utils.db.Database.long_description.__doc__

    def implements_any_of(self, propname):
        """
        Only support for audio files is implemented/
        :param propname: The type of data-support, which is checked if it contains 'audio'
        :return: True if propname is None, it is equal to or contains 'audio', otherwise False.
        """
        if isinstance(propname, (tuple, list)):
            return 'audio' in propname
        elif propname is None:
            return True
        elif isinstance(propname, six.string_types):
            return 'audio' == propname

        # does not implement the given access protocol
        return False

    def get_clients(self, group=None):
        clients = self.__db.clients()
        if group == None:
            return [client.id for client in clients]
        else:
            return [client.id for client in clients if client.group == group]

    get_clients.__doc__ = antispoofing.utils.db.Database.get_clients.__doc__

    def _convert_group_names(self, groups):
        """ convert verification groups to what is used in __db
        """
        if groups is None:
            return None
        group_alias = {'train': 'train', 'devel': 'dev', 'test': 'eval'}
        matched_groups = []
        if isinstance(groups, (tuple, list)):
            for group in groups:
                matched_groups += [group_alias[group]]
        else:
            matched_groups = [group_alias[groups]]
        return matched_groups

    def get_data(self, group):
        """
        Returns either all objects or objects for a specific group

        :param group:
            The groups corresponds to the subset of the ASVspoof data that is used for either training,
            development, or evaluation tasks.
            It can be 'train', 'devel', 'test', or their tuple.

        :return:
            Two lists of File objects (antispoofing.utils.db.File) in the form of [real, attack].
            The first list - real or genuine data and the second list is attacks or spoofed data.
        """
        group = self._convert_group_names(group)
        real = dict(self.__kwargs)
        real.update({'groups': group, 'purposes': 'real'})
        attack = dict(self.__kwargs)
        attack.update({'groups': group, 'purposes': 'attack'})
        return [File(k) for k in self.__db.objects(**real)], \
               [File(k) for k in self.__db.objects(**attack)]

    def get_enroll_data(self, group=None):
        """Returns either all enrollment objects or enrollment objects for a specific group"""
        return self.get_data(group=group)

    get_enroll_data.__doc__ = antispoofing.utils.db.Database.get_enroll_data.__doc__

    def get_train_data(self):
        return self.get_data('train')

    get_train_data.__doc__ = antispoofing.utils.db.Database.get_train_data.__doc__

    def get_devel_data(self):
        return self.get_data('devel')

    get_devel_data.__doc__ = antispoofing.utils.db.Database.get_devel_data.__doc__

    def get_test_data(self):
        return self.get_data('test')

    get_test_data.__doc__ = antispoofing.utils.db.Database.get_test_data.__doc__

    def get_test_filters(self):
        return ('support', 'protocol')

    get_test_filters.__doc__ = antispoofing.utils.db.Database.get_test_filters.__doc__

    def get_filtered_test_data(self, filter):

        def support_filter(obj, filter):
            return obj.get_attacktype() == filter

        def protocol_filter(obj, filter):
            return obj.get_protocol() == filter

        real, attack = self.get_test_data()

        if filter == 'support':
            return {
                'S1': (real, [k for k in attack if support_filter(k, 'S1')]),
                'S2': (real, [k for k in attack if support_filter(k, 'S2')]),
                'S3': (real, [k for k in attack if support_filter(k, 'S3')]),
                'S4': (real, [k for k in attack if support_filter(k, 'S4')]),
                'S5': (real, [k for k in attack if support_filter(k, 'S5')]),
                'S6': (real, [k for k in attack if support_filter(k, 'S6')]),
                'S7': (real, [k for k in attack if support_filter(k, 'S7')]),
                'S8': (real, [k for k in attack if support_filter(k, 'S8')]),
                'S9': (real, [k for k in attack if support_filter(k, 'S9')]),
                'S10': (real, [k for k in attack if support_filter(k, 'S10')]),
            }
        elif filter == 'protocol':
            return {
                'CM': (real, [k for k in attack if protocol_filter(k, 'CM')]),
            }

    get_filtered_test_data.__doc__ = antispoofing.utils.db.Database.get_filtered_test_data.__doc__

    def get_filtered_devel_data(self, filter):

        def support_filter(obj, filter):
            return obj.get_attacktype() == filter

        def protocol_filter(obj, filter):
            return obj.get_protocol() == filter

        real, attack = self.get_devel_data()

        if filter == 'support':
            return {
                'S1': (real, [k for k in attack if support_filter(k, 'S1')]),
                'S2': (real, [k for k in attack if support_filter(k, 'S2')]),
                'S3': (real, [k for k in attack if support_filter(k, 'S3')]),
                'S4': (real, [k for k in attack if support_filter(k, 'S4')]),
                'S5': (real, [k for k in attack if support_filter(k, 'S5')]),
            }
        elif filter == 'protocol':
            return {
                'CM': (real, [k for k in attack if protocol_filter(k, 'CM')]),
            }

        raise RuntimeError("filter parameter should specify a valid filter among `%s'" % str(self.get_test_filters()))

    get_filtered_devel_data.__doc__ = antispoofing.utils.db.Database.get_filtered_devel_data.__doc__

    def get_all_data(self):
        return self.get_data(None)

    get_all_data.__doc__ = antispoofing.utils.db.Database.get_all_data.__doc__
