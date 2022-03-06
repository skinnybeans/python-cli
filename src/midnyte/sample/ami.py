import midnyte.command

def get_amis():
    return [{"ami_id":"ami-1234"}]
class AmiCommand(midnyte.command.CommandMixin):
    def __init__(self):
        pass

    def command_execute(self, arguments):
        # print(f'running instances parser with args: {arguments}')
        print(f'processing ami: {arguments.id}')
        print(get_amis())

    def command_help(self):
        return('Here is some help for amis')

    def command_setup(self, parser):
        print("setting up parser for ami")
        parser.add_argument('-id', help='ID of specific ami', required=True)

    def command_name(self):
        return 'ami'