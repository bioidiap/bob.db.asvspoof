.. vim: set fileencoding=utf-8 :
.. Tue 16 Aug 11:51:35 CEST 2016

.. image:: http://img.shields.io/badge/docs-v1.2.0-yellow.svg
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.asvspoof/v1.2.0/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.svg
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.asvspoof/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.asvspoof/badges/v1.2.0/build.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof/commits/v1.2.0
.. image:: https://gitlab.idiap.ch/bob/bob.db.asvspoof/badges/v1.2.0/coverage.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof/commits/v1.2.0
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof
.. image:: http://img.shields.io/pypi/v/bob.db.asvspoof.svg
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

Complete Bob's `installation`_ instructions. Then, to install this package,
run::

  $ conda install bob.db.asvspoof


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://www.idiap.ch/software/bob/install
.. _mailing list: https://www.idiap.ch/software/bob/discuss
.. _asvspoof: http://datashare.is.ed.ac.uk/handle/10283/853