.. vim: set fileencoding=utf-8 :
.. Pavel Korshunov <Pavel.Korshunov@idiap.ch>
.. Wed Nov 11 15:32:22 CET 2015


.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.db.asvspoof/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.db.asvspoof/master/index.html
.. image:: https://travis-ci.org/bioidiap/bob.db.asvspoof.svg?branch=v1.0.0
   :target: https://travis-ci.org/bioidiap/bob.db.asvspoof
.. image:: https://coveralls.io/repos/bioidiap/bob.db.asvspoof/badge.png
   :target: https://coveralls.io/r/bioidiap/bob.db.asvspoof
.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.db.asvspoof/tree/master
.. image:: http://img.shields.io/pypi/v/bob.db.asvspoof.png
   :target: https://pypi.python.org/pypi/bob.db.asvspoof
.. image:: http://img.shields.io/pypi/dm/bob.db.asvspoof.png
   :target: https://pypi.python.org/pypi/bob.db.asvspoof
.. image:: https://img.shields.io/badge/original-data--files-a000a0.png
   :target: http://datashare.is.ed.ac.uk/handle/10283/853


===================================
ASVspoof Database Interface for Bob
===================================

This package contains a Bob-based access API for the ASVspoof_ Database. The database has been used in the first Automatic Speaker Verification Spoofing and Countermeasures Challenge (ASVspoof 2015). Genuine speech is collected from 106 speakers (45 male, 61 female) and with no significant channel or background noise effects. Spoofed speech is generated from the genuine data using a number of different spooﬁng algorithms. The full dataset is partitioned into three subsets, the first for training, the second for development, and the third for evaluation. More details can be found in the evaluation plan in the summary paper::

	@inproceedings{WuASVspoof2015,
	  title={{ASVspoof} 2015: the First Automatic Speaker Verification Spoofing and Countermeasures Challenge},
	  author={Wu, Zhizheng and Kinnunen, Tomi and Evans, Nicholas and Yamagishi, Junichi and 
		Hanil{\c{c}}i, Cemal and Sahidullah, Md and Sizov, Aleksandr},
	  booktitle={INTERSPEECH},
	  month=sep,
	  address={Dresden, Germany},
	  year={2015},
	  pages={2037-2041}
	} 

This package contains the Bob_-compliant interface implementation with methods to use the database directly from Python with our certified protocols. If you use this package, please cite the following paper::

    @inproceedings{KorshunovInterspeech2016,
        author = {P. Korshunov AND S. Marcel},
        title = {Cross-database evaluation of audio-based spoofing detection systems},
        year = {2016},
        month = sep,
        booktitle = {Interspeech},
        address = {San Francisco, CA, USA},
    }


Installation
------------
To install this package -- alone or together with other `Packages of Bob <https://github.com/idiap/bob/wiki/Packages>`_ -- please read the `Installation Instructions <https://github.com/idiap/bob/wiki/Installation>`_.
For Bob_ to be able to work properly, some dependent packages are required to be installed.
Please make sure that you have read the `Dependencies <https://github.com/idiap/bob/wiki/Dependencies>`_ for your operating system.

Getting the data
----------------
The data can be downloaded from its original ASVspoof_ URL.


Documentation
-------------
For further documentation on this package, please read the `Stable Version <http://pythonhosted.org/bob.db.asvspoof/index.html>`_ or the `Latest Version <https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.db.asvspoof/master/index.html>`_ of the documentation.
For a list of tutorials on this or the other packages ob Bob_, or information on submitting issues, asking questions and starting discussions, please visit its website.


.. _bob: https://www.idiap.ch/software/bob
.. _ASVspoof: http://datashare.is.ed.ac.uk/handle/10283/853



