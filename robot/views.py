from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import pdb,re,json

from .models import *
from .utils import *
# Create your views here.

@csrf_exempt
def init_robo(request):
    if request.method == 'POST':
        robo_name = request.POST['name']
        try:
            r = Robo.objects.create(name=robo_name)
        except:
            return HttpResponse("Please try another name.")
        r.place()
        r.save()
        return HttpResponse("Created successfully.")
    else:
        return HttpResponse(status=405)

@csrf_exempt
def navigate(request):
    if request.method == 'POST':
        robo_id = request.POST['name']
        rcvd_cmd = request.POST['command']
        if robo_id and len(rcvd_cmd) != 0:
            try:
                robo = Robo.objects.get(name=robo_id)
            except:
                return HttpResponse("Invalid Robot Name")
            proc_command = Instruction(rcvd_cmd)
            command_details = proc_command.get_details()
            # return HttpResponse(json.dumps(command_details))
            if command_details:
                final_res = robo_navigate(robo, command_details)
                return HttpResponse(json.dumps(final_res))
            else:
                return HttpResponse("Invalid commands")
        else:
            return HttpResponse("Please post valid Robo Name")
    else:
        return HttpResponse(status=405)

def blank_temp(request):
    return render(request, 'index.html')
