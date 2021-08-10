from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import CreateClientForm, CreateEmployeeForm, ProjectForm, CreateProject, CreateUserForm, CreateTrackerForm
from .filters import ProjectFilter, TrackerFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.db.models import Sum

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'jobs/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='employee')
            user.groups.add(group)
            
            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'jobs/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def UserPage(request):
    myUser = request.user.employee
    projects = Project.objects.all()
    myUserProjects = projects.filter(handled=myUser)

    tracker = Tracker.objects.all()
    myUserTracker = tracker.filter(employee=myUser)

    current_month_jobs = myUserTracker.filter(workedDate__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0))
    tot_hr = current_month_jobs.aggregate(Sum('spentTimeHr'))
    tot_min = current_month_jobs.aggregate(Sum('spentTimeMin'))
    min_hr = tot_min['spentTimeMin__sum'] // 60
    ext_min = tot_min['spentTimeMin__sum'] % 60
    tot_hr = tot_hr['spentTimeHr__sum'] + min_hr
    month_working_hr = "{}h:{}m".format(tot_hr, ext_min)

    tot_filecount = current_month_jobs.aggregate(Sum('fileCount'))
    tot_filecount = tot_filecount['fileCount__sum']

    tot_wip = current_month_jobs.filter(status='WIP').aggregate(Count('status'))
    tot_wip = tot_wip['status__count']

    context = {'myUser':myUser, 'myUserProjects':myUserProjects, 'myUserTracker':myUserTracker, \
        'month_working_hr':month_working_hr, 'tot_filecount':tot_filecount, 'tot_wip':tot_wip}
    return render(request, 'jobs/user.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    clients = Client.objects.all()
    projects = Project.objects.all()
    employees = Employee.objects.all()
    total_clients = clients.filter(status='Active').count()
    total_employees = employees.count()
    total_jobs = projects.filter(status='Exists').count()

    context = {'clients':clients, 'projects':projects, 'employees':employees,\
        'total_clients':total_clients, 'total_employees':total_employees, 'total_jobs':total_jobs}
    return render(request, 'jobs/dashboard.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def clients(request, pk_test):
    client = Client.objects.get(id=pk_test)
    proj = Project.objects.all()
    client_proj = proj.filter(client=client)

    myFilter = ProjectFilter(request.GET, queryset=client_proj)
    client_proj = myFilter.qs

    context = {'client':client, 'client_proj':client_proj, 'client_proj_count':client_proj.count(), 'myFilter':myFilter}
    return render(request, 'jobs/client.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def clientForm(request):
    form = CreateClientForm()
    cstatus = Client.STATUS
    if request.method == "POST":   
        form = CreateClientForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form':form, 'cstatus':cstatus}
    return render(request, 'jobs/client_form.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def projects(request):
    project = Project.objects.all()
    return render(request, 'jobs/project.html', {'projects':project})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee(request):
    employees = Employee.objects.all()
    return render(request, 'jobs/employee.html', {'employees':employees})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employeeForm(request):
    form = CreateEmployeeForm()
    if request.method == "POST":   
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors.as_json())
            form = CreateEmployeeForm()
    context = {'form':form}
    return render(request, 'jobs/employee_form.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEmployee(request, pk):
    emp = Employee.objects.get(id=pk)
    form = CreateEmployeeForm(instance=emp)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee')

    context = {'form':form}
    return render(request, 'jobs/employee_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteFunction(request, pk, myModel):
    if myModel == "employee":
        item = Employee.objects.get(id=pk)
    elif myModel == "project":
        item = Project.objects.get(id=pk)
    elif myModel == "tracker":
        item = Tracker.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item':item, 'myModel':myModel}
    print(context)
    return render(request, 'jobs/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def projectForm(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateProject(initial={'client':client})
    if request.method == "POST":
        form = CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'jobs/project_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'jobs/project_form.html', context)

'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'item':project}
    return render(request, 'jobs/delete.html', context)
'''

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def trackerForm(request, pk):
    emp = Employee.objects.get(name=pk)
    form = CreateTrackerForm(initial={'employee':emp})
    project_details = Project.objects.filter(handled=emp)
    client_ids = project_details.values_list('client', flat=True).distinct()
    client_details = Client.objects.filter(pk__in=list(client_ids))
    jstatus = Tracker.JOBSTATUS
    if request.method == "POST":
        form = CreateTrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'jstatus':jstatus, 'project_details':project_details, 'client_details':client_details}
    return render(request, 'jobs/tracker_form.html', context)    

@login_required(login_url='login')
def tracker(request):
    userRole = request.user.groups.all()[0].name
    if userRole == 'employee':
        track = Tracker.objects.all()
        track = track.filter(employee=request.user.employee)
    else:
        track = Tracker.objects.all()

    mytrackFilter = TrackerFilter(request.GET, queryset=track)
    track = mytrackFilter.qs

    context = {'track':track, 'mytrackFilter':mytrackFilter}
    return render(request, 'jobs/tracker.html', context)