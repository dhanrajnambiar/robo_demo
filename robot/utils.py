import re, pdb

"""Instruction class contains method for parsing the commands. It doesnt  identify the Robo. This just parses the command using parse() method and stores placing details as a dict and moving operations sequentially in an array. This values are returned once get_details() method is called."""

class Instruction(object):
    MV_COMMANDS = set(['MOVE', 'LEFT', 'RIGHT', 'REPORT'])#set of all move commands
    PL_COMMANDS = set(['PLACE', 'NORTH', 'EAST', 'SOUTH', 'WEST'])#set of all placing commands

    def __init__(self, cmmd):
        self.placing_detail = {
            "x_cord":None,
            "y_cord":None,
            "face":None
        }#to store placing details
        self.move_details = []#to store moving details
        self.command_error = False
        self.parse(cmmd)

    def parse(self, cmd):
        pl_details = []
        mv_details = []
        # Commmand Parsing START
        parsed_cmd = re.split(',| ', cmd)
        if 'PLACE' in parsed_cmd:#check for placing details
            p = parsed_cmd.index('PLACE')
            pl_details = parsed_cmd[p:p+4]
            mv_details = parsed_cmd[0:p] + parsed_cmd[p+4:]
        else:
            mv_details = parsed_cmd[:]
        #Command Parsing END
        #Validations of parsed commands START
        if not set(mv_details).issubset(Instruction.MV_COMMANDS):
            self.command_error = True
            return
        for sub_cmd in pl_details:
            if sub_cmd not in Instruction.PL_COMMANDS \
                and not sub_cmd.isnumeric():
                self.command_error = True
                return
        #Validations of parsed commands END
        #storing values to instruction instance START
        if len(pl_details) > 0:#some commands may not contain placing detail
            self.placing_detail['x_cord'] = int(pl_details[1])
            self.placing_detail['y_cord'] = int(pl_details[2])
            self.placing_detail['face'] = pl_details[3]
        self.move_details = mv_details
        #storing values to instruction instance END

    def get_details(self):
        if not self.command_error:#check for valid command
            return {
                "Place":self.placing_detail,
                "Navig":self.move_details
            }
        else:
            return None

"""Below function 'robo_navigate' calls the Robo methods to place and move the Robo according to the Parsed Instruction and record its output to array which is then returned"""

def robo_navigate(r_obj, data):
    outputs = []#Array to store the output of move, report operations
    if all(data['Place'].values()):#check whether all the required placing details are available
        pl_res = r_obj.place(data['Place']['x_cord'],\
                    data['Place']['y_cord'],\
                    data['Place']['face'])
        # outputs.append({"pl_res":pl_res})
        if pl_res['status'] == "Failure":
            outputs.append(pl_res['message'])
    for small_command in data['Navig']:
        if small_command == "MOVE":
            mv_res = r_obj.move()
            r_obj.save()
            # outputs.append({"mv_res":mv_res})
            if mv_res['status'] == "Failure":
                outputs.append(mv_res['message'])
        elif small_command == "RIGHT":
            r_obj.right()
            r_obj.save()
        elif small_command == "LEFT":
            r_obj.left()
            r_obj.save()
        elif small_command == "REPORT":
            outputs.append(r_obj.report())
    return outputs
