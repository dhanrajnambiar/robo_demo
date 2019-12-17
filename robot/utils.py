import re, pdb

class Instruction(object):
    MV_COMMANDS = set(['MOVE', 'LEFT', 'RIGHT', 'REPORT'])
    PL_COMMANDS = set(['PLACE', 'NORTH', 'EAST', 'SOUTH', 'WEST'])

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
        if 'PLACE' in parsed_cmd:
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
        # pdb.set_trace()
        if len(pl_details) > 0:
            self.placing_detail['x_cord'] = int(pl_details[1])
            self.placing_detail['y_cord'] = int(pl_details[2])
            self.placing_detail['face'] = pl_details[3]
        self.move_details = mv_details
        #storing values to instruction instance END

    def get_details(self):
        if not self.command_error:
            return {
                "Place":self.placing_detail,
                "Navig":self.move_details
            }
        else:
            return None

def robo_navigate(r_obj, data):
    outputs = []
    if all(data['Place'].values()):
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
