from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import pdb,re

from .models import *
# Create your views here.
MV_COMMANDS = ['MOVE', 'LEFT', 'RIGHT', 'REPORT']
PL_COMMANDS = ['PLACE', 'NORTH', 'EAST', 'SOUTH', 'WEST']

@csrf_exempt
def init_robo(request):
    if request.method == 'POST':
        robo_name = request.POST['name']
        Robo.objects.create(name=robo_name, x_cordinate=0, y_cordinate=0, direction="NORTH")
        return HttpResponse("Created successfully. Robo at origin faces North")
    else:
        return HttpResponse(status=405)

def validate_command(r_obj, cmd):
    placing_details = []#to store placing details
    moving_details = []#to store moving details
    # Commmand Parsing START
    parsed_cmd = re.split(',| ', cmd)
    if 'PLACE' in parsed_cmd:
        p = parsed_cmd.index('PLACE')
        placing_details = parsed_cmd[p:p+4]
        moving_details = parsed_cmd[0:p] + parsed_cmd[p+4:]
    else:
        moving_details = parsed_cmd[:]
    #Command Parsing END
    temp_x = r_obj.x_cordinate
    temp_y = r_obj.y_cordinate
    temp_f = r_obj.direction
    #Validations of parsed commands START
    if not set(moving_details).issubset(MV_COMMANDS):
        return False
    for sub_cmd in placing_details:
        if sub_cmd not in PL_COMMANDS and not sub_cmd.isnumeric():
            return False
    #Validations of parsed commands END
    #trial of placing position START
    if not placing_details[1] in range(0,6) or not placing_details[2] in range(0,6):
        return False
    else:
        temp_x = placing_details[1]
        temp_y = placing_details[2]
        temp_f = placing_details[3]
    #trial of placing position END
    

@csrf_exempt
def navigate(request):
    if request.method == 'POST':
        robo_id = request.POST['name']
        rcvd_cmd = request.POST['command']
        if robo_id and len(rcvd_cmd) != 0:
            robo = Robo.objects.get(name=robo_id)
            res = validate_command(robo, rcvd_cmd)
        else:
            return HttpResponse("Please post valid Robo Name", status=422)
    else:
        return HttpResponse(status=405)

def blank_temp(request):
    return render(request, 'index.html')
