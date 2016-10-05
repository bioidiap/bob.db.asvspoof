.. vim: set fileencoding=utf-8 :
.. Tue 16 Aug 11:51:35 CEST 2016

.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.db.asvspoof/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bob/bob.db.asvspoof/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.asvspoof/badges/v1.1.2/build.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof/commits/v1.1.2
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof
.. image:: http://img.shields.io/pypi/v/bob.db.asvspoof.png
   :target: https://pypi.python.org/pypi/bob.db.asvspoof
.. image:: http://img.shields.io/pypi/dm/bob.db.asvspoof.png
   :target: https://pypi.python.org/pypi/bob.db.asvspoof


===================================
ASVspoof Database Interface for Bob
===================================

This package is part of the signal-processing and machine learning toolbox
Bob_. It contains a Bob-based access API for the ASVspoof_ Database. The
database has been used in the first Automatic Speaker Verification Spoofing and
Countermeasures Challenge (ASVspoof 2015). Genuine speech is collected from 106
speakers (45 male, 61 female) and with no significant channel or background
noise effects. Spoofed speech is generated from the genuine data using a number
of different spoofing algorithms. The full dataset is partitioned into three
subsets, the first for training, the second for development, and the third for
evaluation. More details can be found in the evaluation plan in the summary
paper::

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


Installation
------------

Follow our `installation`_ instructions. Then, using the Python interpreter
provided by the distribution, bootstrap and buildout this package::

  $ python bootstrap-buildout.py
  $ ./bin/buildout


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://gitlab.idiap.ch/bob/bob/wikis/Installation
.. _mailing list: https://groups.google.com/forum/?fromgroups#!forum/bob-devel
.. _asvspoof: http://datashare.is.ed.ac.uk/handle/10283/853
