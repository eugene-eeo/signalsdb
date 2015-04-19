.. image:: /Users/mango/signalsdb/media/red-signal-light.png
   :align: left
   :scale: 40%

SignalsDB
=========

SignalsDB is an MIT-licensed library written in Python providing
a simple way to query a curated database of Unix signals.

Usage:
------

To explain a Unix signal based on the integer id::

    >>> from signalsdb.api import explain
    >>> explain(13)
    {'action': 'kill',
     'description': 'write on a pipe with no reader',
     'id': 13,
     'signal': 'SIGPIPE'}

Then to query the DB based on the signal name, default actions,
or descriptions, in a case-insensitive way using globs::

    >>> from signalsdb.api import search
    >>> search(signal='sigp*', action='kill', description='P*')
    [{'action': 'kill',
      'description': 'write on a pipe with no reader',
      'id': 13,
      'signal': 'SIGPIPE'},
     {'action': 'kill',
      'description': 'profiling timer alarm',
      'id': 27,
      'signal': 'SIGPROF'}]
