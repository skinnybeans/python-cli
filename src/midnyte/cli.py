'''Module for setting up the cli'''

import argparse

import midnyte.sample.ami
import midnyte.sample.instances
import midnyte.command

def add_subcommand(subparsers, command: midnyte.command.CommandMixin):
    '''Creates a new subparser and points to a function that will be invoked for that subparser'''
    
    parser = subparsers.add_parser(command.command_name(), help=command.command_help())
    parser.set_defaults(command=command.command_execute)
    command.command_setup(parser)

def start():
    parser = argparse.ArgumentParser(description='Testing some arg parsing')
    parser.add_argument( '-log', '--log-level', help='Logging level. default=warning', default='warning')

    subparsers = parser.add_subparsers()
    subparsers.required = True

    add_subcommand(subparsers, midnyte.sample.instances.InstanceCommand())
    add_subcommand(subparsers, midnyte.sample.ami.AmiCommand())

    args = parser.parse_args()
    args.command(args)

if __name__ == "__main__":
    start()
