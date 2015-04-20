"""
    signalsdb.db
    ~~~~~~~~~~~~

    Dynamically initialized global signals database
    with explanations and default actions included.
"""


import signal


NAMES = {
    'SIGABRT': ('core', 'abort program (formerly SIGIOT)'),
    'SIGALRM': ('kill', 'real-time timer expired'),
    'SIGBUS': ('core', 'bus error'),
    'SIGCHLD': ('ignore', 'child status has changed'),
    'SIGCONT': ('ignore', 'continue after stop'),
    'SIGEMT': ('core', 'emulate instruction executed'),
    'SIGFPE': ('core', 'floating-point exception'),
    'SIGHUP': ('kill', 'terminal line hangup'),
    'SIGILL': ('core', 'illegal instruction'),
    'SIGINFO': ('ignore', 'status request from keyboard'),
    'SIGINT': ('kill', 'interrupt program'),
    'SIGIO': ('ignore', 'I/O is possible on a descriptor'),
    'SIGKILL': ('kill', 'kill program'),
    'SIGLIBRT': ('kill', 'real-time library interrupt'),
    'SIGPIPE': ('kill', 'write on a pipe with no readers'),
    'SIGPROF': ('kill', 'profiling timer alarm'),
    'SIGQUIT': ('core', 'quit program'),
    'SIGSEGV': ('core', 'invalid memory reference'),
    'SIGSTOP': ('stop', 'stop (cannot be caught or ignored)'),
    'SIGSYS': ('core', 'non-existent system call invoked'),
    'SIGTERM': ('kill', 'software termination signal'),
    'SIGTHR': ('kill', 'thread interrupt'),
    'SIGTRAP': ('core', 'trace trap'),
    'SIGTSTP': ('stop', 'stop signal generated from keyboard'),
    'SIGTTIN': ('stop', 'background read attempted from control terminal'),
    'SIGTTOU': ('stop', 'background write attempted to control terminal'),
    'SIGURG': ('ignore', 'urgent condition present on socket'),
    'SIGUSR1': ('kill', 'user defined signal 1'),
    'SIGUSR2': ('kill', 'user defined signal 2'),
    'SIGVTALRM': ('kill', 'virtual time alarm'),
    'SIGWINCH': ('ignore', 'Window size change'),
    'SIGXCPU': ('kill', 'cpu time limit exceeded'),
    'SIGXFSZ': ('kill', 'file size limit exceeded')
}


SIGNALS = {
    getattr(signal, k): (k,) + NAMES[k] for k in NAMES if
    hasattr(signal, k)
}
