Intro
-----

This module is in some sense mindlessly simple, preferring to reuse and extend ``argparse``'s built-in sub-parser capabilities rather than invent a new DSL or parsing method. It's primary motivation is adding easy subcommand nesting and running.

Here are some simple examples...

A simple python script::

    # test.py

    from enhanced_argparse import EnhancedArgumentParser as EAP

    main = EAP(prog='main')
    sub1 = EAP(prog='sub1')
    subsub1 = EAP(prog='subsub1')

    main.add_child_parser(sub1)
    sub1.add_child_parser(subsub1)

    main.parse_args()

Then from the command line::

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

Connecting functions to parser commands::

    # test2.py

    from enhanced_argparse import EnhancedArgumentParser as EAP

    def do_something(namespace):
        print "The namespace is", repr(namespace)

    main = EAP(prog='main')
    sub1 = EAP(prog='sub1')
    main.add_child_parser(sub1)
    sub1.set_runner(do_something)

    main.parse_args()

    main.run()

Then from the shell::

    [jcmcken@localhost ~]$ python test2.py sub1
    The namespace is Namespace(_execute=<function do_something at 0x7f0843a0f488>)



