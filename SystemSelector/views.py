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
    l = len(systemsToBeShown)
    ids = []
    for i in range(l):
        ids.append(i)


    i = 0
    while(len(ids) > 0):
        idx = random.randint(0, len(ids)-1)
        systemName = systemsToBeShown[ids[idx]].name

        sys = {}
        sys['id'] = str(i +1)
        i = i + 1
        sys['actualID'] = systemsToBeShown[ids[idx]].id
        ids.pop(idx)
        sys['name'] = systemName

        allSystem.append(sys)
 

    return render(request, 'index.html', {'all_systems': allSystem})


def assign(request):
    if(request.method == 'GET'):
        system = request.GET['systemInput']
    return render(request, 'assign.html', {'system': system})


def show(request):
    allGroup = Group.objects.all()
    c1 = []
    c2 = []

    for grp in allGroup:
        if grp.Subgroup == 'C1':
            c1.append(grp)
        else:
            c2.append(grp)

    constraints = {
        'c1':c1,
        'c2':c2
    }
    return render(request, 'show.html', constraints)


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
    sys_info.taken = True
    sys_info.save()

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
    allSys = System.objects.all()
    for sys in allSys:
        sys.taken = False
        sys.save()
    return redirect('/')
