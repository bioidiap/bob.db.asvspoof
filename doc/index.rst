.. vim: set fileencoding=utf-8 :
.. @author: Pavel Korshunov <Pavel.Korshunov@idiap.ch>
.. @date:   Wed Nov 11 15:06:22 CEST 2015

.. _bob.db.asvspoof:

===========================
ASVspoof Database Interface
===========================

ASVspoof Protocols
------------------

ASVspoof_ database provides three protocols::

	* CM - protocol for presentation attack detection (PAD) experiments. It's short for countermeasure.
	* ASV - protocol for automatic speaker verification (ASV) experiments.
	* AS - protocol that was used in Automatic Speaker Verification Spoofing and Countermeasures Challenge (ASVspoof 2015) with anonymized Test set samples.

All these protocols are supported by `bob.db.asvspoof` DB interface for Bob_.


Getting the data
----------------

The original data and the description of protocols can be downloaded directly from ASVspoof_.


Using this interface 
--------------------

Once the interface package is installed, SQL database file need to be downloaded using the following command:

.. code-block:: sh

    $ .bin/bob_dbmanage.py asvspoof download


This interface can be used to directly query and access the database protocols and samples, or/and in verification `bob.bio.` and PAD `bob.pad.` frameworks of Bob toolkit.

The database filelist can be queried via the following command line:

.. code-block:: sh

    $ .bin/bob_dbmanage.py asvspoof dumplist --help

To use the database in verification experiments within `bob.bio.` framework, a `bob.bio.database` entry point need to be defined in the `setup.py` file of the package that would run these experiments as so, as follows:

.. code-block:: python

        'bob.bio.database': [
            'asvspoof             = bob.path.to.config.file:database',
	]

The config file (other ways to defined the database are also available in Bob_, please see database API documentation) would then initialize the `database` with the path to the directory where the actual database sample are located, as follows:

.. code-block:: python

	import bob.bio.db
	asvspoof_input_dir = "PATH_TO_DATA"
	database = bob.bio.db.ASVspoofBioDatabase(
	    protocol = 'ASV',
	    original_directory=asvspoof_input_dir,
	    original_extension=".wav",
	    training_depends_on_protocol=True,
	)

Similarly, for PAD experiments, an entry point `bob.pad.database` should be defined in `setup.py` and `bob.pad.db.ASVspoofPadDatabase` should be defined in the config file.

Specifying `bob.bio.database` and/or `bob.pad.database` entry points ensures that the verification and/or PAD frameworks can find and use the database.


.. _bob: https://www.idiap.ch/software/bob
.. _ASVspoof: http://datashare.is.ed.ac.uk/handle/10283/853
.. _idiap: http://www.idiap.ch


