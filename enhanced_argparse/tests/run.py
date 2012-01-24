import unittest
import base

TESTS = (
    'enhanced_argparse.tests.base',
)

def get_test_suite(tests):
    return unittest.defaultTestLoader.loadTestsFromNames(tests)

def get_test_runner(verbosity=2):
    return unittest.TextTestRunner(verbosity=verbosity)

if __name__ == '__main__':
    suite = get_test_suite(TESTS)
    runner = get_test_runner()
    runner.run(suite)
