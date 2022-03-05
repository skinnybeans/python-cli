
def get_instances():
    return [{"instance_id":"i-1234"}]

def execute(arguments):
    print(f'running instances parser with args: {arguments}')

def parser_help():
    return "Basic module to help manipuate instances"

def parser_setup(parser):
    print("setting up parser for instances")
    
    parser.add_argument('-id', help='ID of specific instance', required=True)