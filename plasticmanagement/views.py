import datetime

from django.shortcuts import render
import os

from plasticmanagement.forms import UserForm, LoginForm, WastageForm
from plasticmanagement.models import UserModel, WastageModel
from plasticmanagement.service import getwastages

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

def login(request):

    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            if uname == "admin@gmail.com" and upass == "Admin123":
                request.session['username'] = "admin"
                request.session['role'] = "admin"
            else:

                user = UserModel.objects.filter(username=uname, password=upass).first()

                if user is not None:
                    request.session['username'] = uname
                    request.session['role'] = user.usertype
                else:
                    return render(request, 'index.html', {"message": "Invalid Credentials"})

            return render(request, "wastages.html",{"wastages": getwastages(request.session['role'], request.session['username'])})

        else:
            return render(request, 'index.html', {"message": "Invalid Form"})

    return render(request, 'index.html', {"message": "Invalid Request"})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

#=======================================================================================================

def adduser(request):

    if request.method == "POST":

        userForm = UserForm(request.POST)

        usertype=""
        status = False

        if userForm.is_valid():

            userModel = UserModel()

            usertype=userForm.cleaned_data["usertype"]
            userModel.username = userForm.cleaned_data["username"]
            userModel.password = userForm.cleaned_data["password"]
            userModel.name = userForm.cleaned_data["name"]
            userModel.mobile = userForm.cleaned_data["mobile"]
            userModel.address = userForm.cleaned_data["address"]
            userModel.usertype = userForm.cleaned_data["usertype"]

            user = UserModel.objects.filter(username=userModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    userModel.save()
                    status = True
                except:
                    status = False

        if status:
            if usertype=="agent":
                return render(request, 'adduser.html', {"message": "Agent Added Successfully"})
            elif usertype=="user":
                return render(request, 'index.html', {"message": "User Added Successfully"})
        else:

            if usertype=="agent":
                return render(request, 'adduser.html', {"message": "Agent AlReady Exist"})
            elif usertype=="user":
                return render(request, 'index.html', {"message": "User AlReady Exist"})

    return render(request, 'index.html', {"message": "invalid request"})

def adminviewusers(request):
    return render(request, "users.html", {"users":UserModel.objects.filter(usertype='agent')})

def deleteuser(request):
    userid=request.GET['userid']
    UserModel.objects.filter(username=userid).delete()
    return render(request, "users.html", {"users":UserModel.objects.all()})

#=========================================================================================================

def addwastageaction(request):

    wastageForm = WastageForm(request.POST,request.FILES)

    if wastageForm.is_valid():

        WastageModel(

            wastagename = wastageForm.cleaned_data['wastagename'],
            image =wastageForm.cleaned_data['image'],
            cost = wastageForm.cleaned_data['cost'],
            quantity = wastageForm.cleaned_data['quantity'],
            address = wastageForm.cleaned_data['address'],
            category = wastageForm.cleaned_data['category'],

            customerid=request.session['username'],
            assignedto = "",
            collectiondate = wastageForm.cleaned_data['collectiondate'],
            adminstatus = "no",
            status = "",
            date = datetime.datetime.now()

        ).save()

        return render(request, "wastages.html",{"wastages":getwastages(request.session['role'],request.session['username'])})

    else:
        return render(request, "addwastage.html", {"message": "in valid request"})

def viewwastages(request):
    return render(request, "wastages.html",{"wastages":getwastages(request.session['role'],request.session['username'])})

def acceptorrejectwastage(request):

    status=WastageModel.objects.get(id=request.GET['wastageid']).adminstatus

    if status=="yes" or status=="":
        WastageModel.objects.filter(id=request.GET['wastageid']).update(adminstatus="no")
    elif status=="no":
        WastageModel.objects.filter(id=request.GET['wastageid']).update(adminstatus="yes")

    return render(request, "wastages.html",{"wastages": getwastages(request.session['role'], request.session['username'])})

def getwastage(request):
    if request.GET['type']=="assign":
        return render(request, "assignwastage.html",{"wastageid":request.GET['wastageid'],"agents":UserModel.objects.filter(usertype='agent')})
    elif request.GET['type']=="update":
        return render(request, "agentupdate.html",{"wastageid":request.GET['wastageid']})

def assignwastage(request):
    WastageModel.objects.filter(id=request.GET['wastageid']).update(assignedto=request.GET['assignedto'])
    return render(request, "wastages.html",{"wastages": getwastages(request.session['role'], request.session['username'])})

def agentwastageupdate(request):
    WastageModel.objects.filter(id=request.GET['wastageid']).update(status=request.GET['status'])
    return render(request, "wastages.html",{"wastages": getwastages(request.session['role'], request.session['username'])})

def deletewastage(request):
    WastageModel.objects.get(id=request.GET['wastageid']).delete()
    return render(request, "wastages.html",{"wastages":getwastages(request.session['role'],request.session['username'])})