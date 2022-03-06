import argparse
import midnyte

import midnyte.sample.ami
import midnyte.sample.instances
import midnyte.command

def add_subcommand(subparsers, command: midnyte.command.CommandMixin):
    parser = subparsers.add_parser(command.command_name(), help=command.command_help())
    parser.set_defaults(command=command.command_execute)
    command.command_setup(parser)

def start():
    parser = argparse.ArgumentParser(description='Testing some arg parsing')
    parser.add_argument( '-log', '--log-level', help='Logging level. default=warning', default='warning')

    subparsers = parser.add_subparsers()
    subparsers.required = True

    # add_subcommand(subparsers, 'ami', midnyte.sample.ami)
    add_subcommand(subparsers, midnyte.sample.instances.InstanceCommand())
    add_subcommand(subparsers, midnyte.sample.ami.AmiCommand())


    args = parser.parse_args()
    args.command(args)

if __name__ == "__main__":
    start()
