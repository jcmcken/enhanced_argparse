
import unittest
from enhanced_argparse import EnhancedArgumentParser as EAP

P1, P2 = 'parser1', 'parser2'

class EAPTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = EAP(prog=P1)
        self.parser.add_argument('-t')

    def testRunner(self):
        self.parser.set_runner(lambda ns: ns.t)
        self.parser.parse_args(['-t', 'foobar'])
        self.assertEquals(self.parser.run(), 'foobar')

    def testInvalidArg(self):
        self.assertRaises(
            SystemExit, self.parser.parse_args, ['foobar']
        )
                 
class EAPNestedTestCase(unittest.TestCase):

    def setUp(self):
        self.parser1 = EAP(prog=P1)
        self.parser2 = EAP(prog=P2)
        self.parser2.add_argument('foo')
        self.parser2.set_runner(lambda ns: 'bar')
        self.parser1.add_child_parser(self.parser2)

    def testChildName(self):
        self.assertEquals(
            self.parser2.prog, "%s %s" % (P1, P2)
        )

    def testSubcommand(self):
        self.parser1.parse_args([P2, 'foo'])
        self.assertEquals(self.parser1.run(), 'bar')





