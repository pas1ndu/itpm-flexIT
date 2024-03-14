from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.template import RequestContext

# Create your views here.

#def cvacancy(request):
    #return render(request, 'vacancies/cvacancy.html')

def jrecuriting(request):

    vacan = vacancy.objects.all()

    return render(request, 'vacancies/jrecuriting.html', {'vacan':vacan})
    # return render(request, 'vacancies/jrecuriting.html')

def uvacancy(request):
    return render(request, 'vacancies/uvacancy.html')

def deletecon(request):
    return render(request, 'vacancies/deletecom.html')



def cvacancy(request):

    form = vacancyform()
    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = vacancyform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('jrecruiting')
        


    context = {'form':form}

    return render(request, 'vacancies/cvacancy.html',context)


def updateComVa(request, pk):

    vacan = vacancy.objects.get(id=pk)
    form = vacancyform(instance=vacan)

    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = vacancyform(request.POST, instance=vacan)
        if form.is_valid():
                form.save()
                return redirect('jrecruiting')

    context = {'form':form}
    return render(request, 'vacancies/cvacancy.html',context)


def deleteComVa(request, pk):
    vacan = vacancy.objects.get(id=pk)
    if request.method == "POST":
        vacan.delete()
        return redirect('jrecruiting')

    context = {'item':vacan}
    return render(request, 'vacancies/deletecom.html', context)



def readcvbtn(request):
    cvdata = Cvdetails.objects.all()

    return render(request, 'CVpages/dil_preBtn.html', {'cvdata': cvdata})



def ogcreatehtml(request):

    form = CvDetailsForm()
    if request.method == 'POST':
        #print('',request.POST)
        form = CvDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def updatecv(request, pk):

    cvdata = Cvdetails.objects.get(id=pk)
    form = CvDetailsForm(instance = cvdata)

    if request.method == 'POST':
        form = Cvdetails(request.POST, instance = cvdata)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def deleteCv(request, pk):
    cvdata = Cvdetails.objects.get(id=pk)

    if request.method == 'POST':
            cvdata.delete()
            return redirect('/button')


    context = {'form':cvdata}
    return render(request, 'CVpages/dilcvdiscard.html', context)


# sathma
def comLogin(request):
	# form = ComRegisterForm()
	if request.method == 'POST':
		email = request.POST.get('username')
		password = request.POST.get('password')

		comregister = authenticate(request, email=email, password=password)

		if comregister is not None:
			login(request, comregister)
			redirect('/comprofile')

		else:
			messages.info(request, 'Email OR Password is not correct')	


	context={}
	return render(request,'sprint1/login.html')


def registerPage(request):
	form = ComRegisterForm()
	if request.method == 'POST':
		form = ComRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('company_name')
			messages.success(request, 'Account was created for ' + user)
			return redirect('/login')

	context={'form':form}
	return render(request,'sprint1/register.html',context)




def dashboard(request):
	return render(request,'sprint1/dashboard.html')

def Sreg(request):
	return render(request,'sprint1/register.html')



def comprofile(request):

	company = comregister.objects.all()

	return render(request,'sprint1/comprofile.html', {'company':company})


def updateComp(request, pk):

    comp = comregister.objects.get(id=pk)
    form = ComRegisterForm(instance=comp)

    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = ComRegisterForm(request.POST, instance=comp)
        if form.is_valid():
                form.save()
                return redirect('/comprofile')

    context = {'form':form}
    return render(request, 'sprint1/register.html',context)


def deleteComp(request, pk):
    comp = comregister.objects.get(id=pk)
    if request.method == "POST":
        comp.delete()
        return redirect('/loginPage')

    context = {'forms':comp}
    return render(request, 'sprint1/login.html', context)




# pasindu
def login(request):
    return render(request, 'flexituser/login.html')



def register(request):

    form = StuUserForm()
    if request.method == 'POST':
        # print ('Printing Post', request.POST)
        form = StuUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')


    context = {'form': form} 
    return render(request, 'flexituser/registration.html', context)  



def stuProfile(request):

	student = Student.objects.all()
	return render(request,'flexituser/studentprofile.html', {'student':student})

def updatestu(request, pk):

    stu = Student.objects.get(id=pk)
    form = StuUserForm(instance=stu)

    if request.method == 'POST':
        #print('printing POST:', request.POST)
        form = StuUserForm(request.POST, instance=stu)
        if form.is_valid():
                form.save()
                return redirect('/stuProfile')

    context = {'form':form}
    return render(request, 'flexituser/registration.html',context)

def deletestu(request, pk):
    stu = Student.objects.get(id=pk)
    if request.method == "POST":
        stu.delete()
        return redirect('/login')

    context = {'forms':stu}
    return render(request, 'flexituser/login.html', context)
