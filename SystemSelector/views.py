from django.shortcuts import render, redirect
from .models import Group, System
import random

def home(request):
    all_systems = System.objects.all()
    systemsToBeShown = []

    for system in all_systems:
        if system.taken == False:
            systemsToBeShown.append(system)


    allSystem = []
    for i in range(int(len(systemsToBeShown)/2)):
        j = random.randint(i+1, len(systemsToBeShown)-1)
        temp = systemsToBeShown[i]
        systemsToBeShown[i] = systemsToBeShown[j]

        systemUnit = {}
        systemUnit.clear()

        systemUnit['randomid'] = i
        systemUnit['system'] = systemsToBeShown[i]

        allSystem.append(systemUnit)

    i = int(len(systemsToBeShown)/2)
    while i < len(systemsToBeShown):
        systemUnit = {}
        systemUnit['randomid'] = i
        systemUnit['system'] = systemsToBeShown[i]

        allSystem.append(systemUnit)

    return render(request, 'index.html', {'all_systems': allSystem})


def assign(request):
    if(request.method == 'GET'):
        system = request.GET['systemInput']
    return render(request, 'assign.html', {'system': system})


def show(request):
    return render(request, 'show.html')


def save(request):
    if(request.method == 'POST'):
        system = request.POST['systemName']

        gname = request.POST['gname']
        subgroup = request.POST['subgroup']
        gleader = request.POST['gleader']
        mem1 = request.POST['mem1']
        mem2 = request.POST['mem2']
        mem3 = request.POST['mem3']
        mem4 = request.POST['mem4']
        mem5 = request.POST['mem5']

    sys = System.objects.all()
    for s in sys:
        if(system in s.name):
            sys_info = s
    grp = Group()
    s.taken = True
    s.save()

    grp.name = gname
    grp.project_system = sys_info
    grp.Subgroup = subgroup
    grp.leader = gleader
    grp.member_name_1 = mem1
    grp.member_name_2 = mem2
    grp.member_name_3 = mem3
    grp.member_name_4 = mem4
    grp.member_name_5 = mem5

    grp.save()
    return redirect('/')


def clear(request):
    return render(request, 'index.html')
