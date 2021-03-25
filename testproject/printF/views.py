from django.shortcuts import render
from django.http import JsonResponse
from .models import dataStore, userDetail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def renderHomepage(request):
    if request.method == "GET":
        return render(request, 'index.html')

# Create your views here.
def printVals(request):
    if request.method == "GET":
        print(request.GET)
        return JsonResponse({"ok":"OK"})

def addVals(request):
    if request.method == "GET":
        print(request.GET)
        s = int(request.GET['a']) + int(request.GET['b'])
        return JsonResponse({'sum': s})
#annotations - django
@csrf_exempt
def storeDB(request):
    if request.method == "POST":
        print(request.POST)
        x = dataStore(name = request.POST['a'], age = request.POST['b'])
        x.save()
        return JsonResponse({"result": 'success'})

def fetchStore(request):
    if request.method == "GET":
        print(request.GET)
        x = list(dataStore.objects.values())
        print(x)
        return JsonResponse({"result":x})

def fetchByID(request):
    if request.method == "GET":
        print(request.GET)
        x = dataStore.objects.filter(id=request.GET['id'])
        x = list(x.values())
        return JsonResponse({'result': x})

def clearDB(request, id):
    print(request.GET)
    if request.method == "GET":
        x = dataStore.objects.get(id=id)
        x.delete()
        return JsonResponse({"result": "deletion success"})

@csrf_exempt
def userregistration(request):
    if request.method == "GET":
        return render(request, 'custom/register.html')
    if request.method == "POST":
        x = userDetail(firstname=request.POST['firstname'], surname=request.POST['surname'], email=request.POST['email'], date=request.POST['date'], month=request.POST['month'], year=request.POST['year'], sex=request.POST['gender'])
        x.save()
        return render(request, 'custom/register.html')

@csrf_exempt
def signin(request):
    if request.method == "GET":
        return render(request, 'custom/signin.html')
    if request.method == "POST":
        #signin username password match-up
        inputName = request.POST.get('username')
        inputPassword = request.POST.get('password')
        print(inputName,inputPassword)
        dbObj = list(userDetail.objects.filter(name=inputName))
        print(dbObj)
        if len(dbObj)!=0:
            for o in dbObj:
                if o.password==inputPassword:
                    return render(request, 'welcome.html')
            return render(request, 'error.html')
        else:
            return render(request, 'error.html')

def signupDjango(request):
    '''if request.user.is_authenticated:
        return render(request, 'welcome.html')'''

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'welcome.html')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def signinDjango(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            form = AuthenticationForm()
            return render(request, 'signin.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

@csrf_exempt
def signoutDjango(request):
    if request.method == "GET":
        logout(request)
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            form = AuthenticationForm()
            return render(request, 'signin.html', {'form': form})