from ast import arg
import midnyte.command

def get_instances():
    return [{"instance_id":"i-1234"}]

def execute(arguments):
    print(f'running instances parser with args: {arguments}')

def parser_help():
    return "Basic module to help manipuate instances"

def parser_setup(parser):
    print("setting up parser for instances")
    
    parser.add_argument('-id', help='ID of specific instance', required=True)

class InstanceCommand(midnyte.command.CommandMixin):
    def __init__(self):
        pass

    def command_execute(self, arguments):
        # print(f'running instances parser with args: {arguments}')
        print(f'processing instance: {arguments.id}')
        print(get_instances())

    def command_help(self):
        return('Here is some help for instances')

    def command_setup(self, parser):
        print("setting up parser for instances")
        parser.add_argument('-id', help='ID of specific instance', required=True)

    def command_name(self):
        return 'instances'