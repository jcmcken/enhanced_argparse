from distutils.core import setup

setup(
    name='enhanced_argparse',
    version='0.1.0',
    description='A simple extension for argparse',
    long_description=(
        "No special DSL. No magic. Just a simple, no-nonsense extension "
        "of argparse's main ArgumentParser class. Adds convenience "
        "methods for creating nested subcommands that hook up easily "
        "to user-defined functions"
    ),
    author='Jon McKenzie',
    author_email='jcmcken@gmail.com',
    url='http://github.com/jcmcken/enhanced_argparse',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    requires=['argparse'],
    license='LICENSE',
    packages=['enhanced_argparse'],
)
