
def get_amis():
    return [{"ami_id":"ami-1234"}]

def execute(arguments):
    print(f'running ami parser with args: {arguments}')

def parser_help():
    return "Basic module to help manipuate AMIs"

def parser_setup(parser):
    print("setting up parser for ami")
    parser.add_argument('-id', help='ID of specific AMI', required=True)