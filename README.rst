|logo| SignalsDB
================

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

Then to query the signals DB based on the signal name or action
in a case insensitive way using regexes::

    >>> from signalsdb.api import search
    >>> search(signal='sigp\w', action='kill')
    [{'action': 'kill',
      'description': 'write on a pipe with no reader',
      'id': 13,
      'signal': 'SIGPIPE'},
     {'action': 'kill',
      'description': 'profiling timer alarm',
      'id': 27,
      'signal': 'SIGPROF'}]


.. |logo| image:: https://raw.githubusercontent.com/eugene-eeo/signalsdb/master/media/red-signal-light.png
