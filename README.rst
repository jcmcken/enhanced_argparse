Intro
-----

This module is in some sense mindlessly simple, preferring to reuse and extend ``argparse``'s built-in sub-parser capabilities rather than invent a new DSL or parsing method. It's primary motivation is adding easy subcommand nesting and running.

Some simple examples:

A simple python script...::

    # test.py

    from enhanced_argparse import EnhancedArgumentParser as EAP

    main = EAP(prog='main')
    sub1 = EAP(prog='sub1')
    subsub1 = EAP(prog='subsub1')

    main.add_child_parser(sub1)
    sub1.add_child_parser(subsub1)

    main.parse_args()

Then from the command line...::

    [jcmcken@localhost ~]$ python test.py -h
    usage: main [-h] {sub1} ...
    
    positional arguments:
      {sub1}
    
      optional arguments:
        -h, --help  show this help message and exit

    [jcmcken@localhost ~]$ python test.py sub1 -h
    usage: main sub1 [-h] {subsub1} ...

    positional arguments:
      {subsub1}

    [jcmcken@localhost ~]$ python test.py sub1 subsub1 -h
    usage: main sub1 subsub1 [-h]

    optional arguments:
      -h, --help  show this help message and exit


