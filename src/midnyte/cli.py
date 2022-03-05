import argparse
import midnyte

import midnyte.sample.ami
import midnyte.sample.instances

def add_subcommand(subparsers, name, module):
    parser = subparsers.add_parser(name, help=module.parser_help())
    parser.set_defaults(module=module)
    module.parser_setup(parser)

def start():
    parser = argparse.ArgumentParser(description='Testing some arg parsing')
    parser.add_argument( '-log', '--log-level', help='Logging level. default=warning', default='warning')

    subparsers = parser.add_subparsers()
    subparsers.required = True

    add_subcommand(subparsers, 'ami', midnyte.sample.ami)
    add_subcommand(subparsers, 'instances', midnyte.sample.instances)


    args = parser.parse_args()
    # print(args)
    # getattr(args.module, 'execute')(args)
    args.module.execute(args)

if __name__ == "__main__":
    start()
