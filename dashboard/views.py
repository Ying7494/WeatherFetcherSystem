from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from datetime import datetime
from dashboard.models import User
from dashboard.models import Weather


import requests
import hashlib
import json
import operator


# Dashboard Page
def dashboard(request):
    checkSession(request)

    if not request.session.get("isLogin"):
        return HttpResponseRedirect('/login/')
    else:
        if request.GET.get('city'):
            return render(request, 'index.html', {
                'username': request.session["username"],
                'city': request.GET.get('city'),
            })
        else:
            return render(request, 'index.html', {
                'username': request.session["username"],
                'city': "",
            })


# Login Page
def login(request):
    checkSession(request)
    
    if request.session.get("isLogin"):
        return HttpResponseRedirect('/dashboard/')
    return render(request, 'login.html')


# Login API
def login_post(request):
    checkSession(request)

    response = { "data" : "null" }
    if request.POST['username'] and request.POST['password']:
        # Checking password
        try:
            user = User.objects.get(username=request.POST['username'])
            if user.password == md5(request.POST['password']):
                # Write username into session
                request.session["username"] = request.POST['username']
                # Change Login Status
                request.session["isLogin"] = 1
                response['status'] = 200
            else:
                response['status'] = 403

        except:
            response['status'] = 403
    else:
        response['status'] = 400

    return render(request, "api.html", response)


# Logout API
def logout_post(request):
    response = { "data" : "null" }
    
    try:
        request.session["isLogin"] = 0
        request.session["username"] = None
        response['status'] = 200
        return HttpResponseRedirect('/login/')

    except:
        response['status'] = 500

    return render(request, "api.html", response)



# Get Weather API
def getWeatherAPI(request):
    checkSession(request)
    response = { "data" : "null" }
    

    if not request.session.get("isLogin"):
        response['status'] = 403
        return render(request, 'api.html', response)
    else:
        response['status'] = 200
        if request.GET.get('city'):
            qs = serializers.serialize("json", Weather.objects.filter(city=request.GET.get('city')).order_by('id').reverse())
            return HttpResponse(qs, content_type="application/json")
        else:
            qs = serializers.serialize("json", Weather.objects.all().order_by('id').reverse())
            return HttpResponse( qs, content_type="application/json")


# Weather REST API
def weatherAPI(request):
    response = { "data" : "null" }
    if request.GET.get('username') and request.GET.get('password'):
        # Checking password
        try:
            user = User.objects.get(username=request.GET.get('username'))
            if user.password == md5(request.GET.get('password')):
                # Get Weather from DB
                response['data'] = serializers.serialize("json", Weather.objects.filter(city=request.GET.get('city')))
                response['status'] = 200
            else:
                response['status'] = 403

        except Exception as e:
            response['status'] = e
    else:
        response['status'] = 400

    return render(request, "api.html", response)


# Get Weather Data form CWB
def getWeather():
    response = { "data" : "null" }

    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization=CWB-A20AB53B-3784-4EF8-BAFC-78280515D1D9&downloadType=WEB&format=JSON'
    r = requests.get(url)
    response['status'] = r.status_code
    data = json.loads(r.text)
    

    for value in data["cwbopendata"]["location"]:
        obsTime = value["time"]["obsTime"]

        if operator.eq(value["stationId"], "466920"): # Taipei
            insertDB(value["weatherElement"],"01",obsTime)
            
        if operator.eq(value["stationId"], "466880"): # New Taipei
            insertDB(value["weatherElement"],"06",obsTime)

        if operator.eq(value["stationId"], "467050"): # Taoyuan
            insertDB(value["weatherElement"],"08",obsTime)

    return None


# Check Session
def checkSession(request):
    if not request.session.session_key: # Check Session ID doesn't exist
        request.session.create()
        request.session["isLogin"] = 0
    return None


# MD5 Encrypt
def md5(data):
    m = hashlib.md5()
    m.update(data.encode("utf-8"))
    h = m.hexdigest()
    return h


# Insert Weather Data
def insertDB(elm,cityID,obsTime):
    TEMP = None
    HUMD = None
    PRES = None
    WDIR = None
    WDSD = None
    for subvalue in elm:
        if operator.eq(subvalue["elementName"],"TEMP"):
            TEMP = subvalue["elementValue"]["value"]
        if operator.eq(subvalue["elementName"],"HUMD"):
            HUMD = subvalue["elementValue"]["value"]
        if operator.eq(subvalue["elementName"],"PRES"):
            PRES = subvalue["elementValue"]["value"]
        if operator.eq(subvalue["elementName"],"WDIR"):
            WDIR = subvalue["elementValue"]["value"]
        if operator.eq(subvalue["elementName"],"WDSD"):
            WDSD = subvalue["elementValue"]["value"]
    try:
        p = Weather(city=cityID, temp=TEMP, humd=HUMD, pres=PRES, wdir=WDIR, wdsd=WDSD, recordTime=obsTime)
        p.save()
        return True
    except:
        return False


