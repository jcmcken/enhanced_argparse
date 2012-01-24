import argparse

class EnhancedArgumentParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        argparse.ArgumentParser.__init__(self, *args, **kwargs)
        self._runner = lambda: False
        self._current_subparser = None

    def add_child_parser(self, parser):
        if self._current_subparser is None:
            self._current_subparser = self.add_subparsers()

        name = getattr(parser, 'prog')
        help = getattr(parser, 'description', None)

        parser.prog = '%s %s' % (self._current_subparser._prog_prefix, name)

        if help:
            choice_action = self._current_subparser._ChoicesPseudoAction(name, help)
            self._current_subparser._choices_actions.append(choice_action)

        self._current_subparser._name_parser_map[name] = parser
        return parser
    
    def parse_args(self):
        namespace = argparse.ArgumentParser.parse_args(self)
        if hasattr(args, '__execute'):
            self._runner = lambda: args.__execute(namespace)
        return namespace

    def set_runner(self, func):
        self.set_defaults(__execute=func)

    def run(self):
        self._runner()
