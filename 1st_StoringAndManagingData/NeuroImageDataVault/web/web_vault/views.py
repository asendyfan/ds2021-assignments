from django.shortcuts import render
from django.shortcuts import redirect
from . import models
import hashlib

from .get_data.patients import getPatients, getPatient, getPatientsLen
from .get_data.projects import getProjectData, getProjectsList
from .get_data.sessions import getSessions
from .get_data.stimulus import getStimulus

from django.http import HttpResponse

from django.views.generic import View, TemplateView

from .get_data.downloads import downloadData

def if_login(function):
    def wrapper(request, *args, **kwargs):
        print('if login')
        if not request.session.get('is_login', None):
            return redirect('/login/')
        else: 
            return function(request, *args, **kwargs)
    return wrapper

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'index/index.html', {'projects':getProjectsList()})

@if_login
def project(request, id):
    # get_object_or_404({'id':'xxx'}, pk=id)
    # data = getProjectData(id)
    # return render(request, 'project/project.html', {'data':data, 'is_summary':True, 'experimentid':id})
    return redirect(id+'/sessions')

@if_login
def projectPatients(request, id):
    # data = getProjectData(id)
    data['results'] = getPatients(id)
    return render(request, 'project/project.html', { 'is_patients':True })

@if_login
def projectSessions(request, id):
    data = getProjectData(id)
    sessions = getSessions(id)
    return render(request, 'project/project.html', {'data':data, 'sessions':sessions, 'is_sessions':True, 'experimentid':id})

@if_login
def stimulus(request, id, sessionid):
    data = getStimulus(sessionid)
    patients = getPatients(sessionid)
    patientsLen = getPatientsLen(sessionid)
    # print(123,id, data, )
    return render(request, 'stimulus.html', {'experimentid':id,'sessionid':sessionid,'data':data, 'patientsLen':patientsLen})

@if_login
def endpoint(request, id, sessionid, stimulusid):
    # stimulus = getStimulus(sessionid)
    # return render(request, 'endpoint.html', {'experimentid':id,'sessionid':sessionid, 'stimulusid':stimulusid})
    defaulttype = None
    if id == 'exp1':
        defaultmethod = 'fNIRS'
        defaulttype = 'oxy'
    else:
        defaultmethod='DownloadFNIRS'
        # defaulttype = 'xx'
    return redirect('/{}/{}/{}/method_{}/type_{}'.format(id, sessionid, stimulusid, defaultmethod, defaulttype))

@if_login
def endpointWithType(request, id, sessionid, stimulusid, endpointmethod, endpointtype):
    # stimulus = getStimulus(sessionid)
    types = []
    if id == 'exp1':
        types = ['oxy', 'deoxy', 'total', 'mes_wl1', 'mes_wl2']
        methods = ['fNIRS']
    else:
        methods = ['DownloadFNIRS', 'EEG']

    return render(request, 'endpoint.html', {
        'experimentid':id,
        'sessionid':sessionid, 
        'stimulusid':stimulusid,
        'methods':methods, 'types':types, 'typesLen':len(types),
        'endpointmethod':endpointmethod, 
        'endpointtype':endpointtype
    })

@if_login
def endpointDownload(request, id, sessionid, stimulusid):
    downloadData(sessionid, stimulusid)
    fname = "{}_{}.zip".format(sessionid, stimulusid)
    return HttpResponse(open("web_vault/get_data/download_temp/{}_{}.zip".format(sessionid, stimulusid), 'rb'), 
        content_type='application/zip', headers={'Content-Disposition': 'attachment; filename='+fname}
    )
    # print(zipfile)
    # 

@if_login
def patient(request, id, sessionid, stimulusid, type):
    data = getPatient()
    return render(request, 'patient.html', {
        'data':data, 'experimentid':id, 'sessionid':sessionid, 
        'stimulusid':stimulusid, 'type':type
    })



def login(request):
    if request.session.get('is_login', None):  # 不允许重复Login
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = models.User.objects.get(name=username)
        except:
            message = 'User not exist！'
            return render(request, 'login/login.html', {'message': message})

        if user.password == hash_code(password):
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('/')
        else:
            message = 'Incorrect password！'
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def register(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == 'POST':

        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        same_name_user = models.User.objects.filter(name=username)
        if same_name_user:
            message = 'The user already exists！'
            return render(request, 'login/register.html', locals())
        same_email_user = models.User.objects.filter(email=email)
        if same_email_user:
            message = 'The email has been registered！'
            return render(request, 'login/register.html', locals())

        new_user = models.User()
        new_user.name = username
        new_user.password = hash_code(password)
        new_user.email = email
        new_user.save()

        return redirect('/login/')
    return render(request, 'login/register.html', locals())

def forgot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user_email = models.User.objects.get(email=email)
        except:
            message = 'The email is not registered！'
            return render(request, 'login/forgot.html', {'message': message})

        if user_email.email == email:
            return redirect('/reset/')

    return render(request, 'login/forgot.html')


def reset(request):
    if request.method == 'POST':
        return render(request, 'login/login.html', locals())
    return render(request, 'login/reset.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未Login，也就没有Logout一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")

