from django.shortcuts import render
from cvat.apps.authentication.decorators import login_required
from .models import Instruction

# Create your views here.

@login_required
def InstructionView(request,tid):
    instruction_text = Instruction.objects.get(pk=tid)
    instruction_id = tid
    context={
        "instruction_text":instruction_text,
        "instruction_id":instruction_id,
        'base_url': "{0}://{1}/".format(request.scheme, request.get_host())
    }
    print(context.get("instruction_id"))
    return render(request,"./instruction.html",context)