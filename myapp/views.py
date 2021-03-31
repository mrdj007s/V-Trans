from django.shortcuts import (
    render, 
    HttpResponse,
    redirect,
    #render_to_response
)
from .models import (
    bookvehicle, 
    proceed,
    contactus,
    summary,
    payment
)
from .models import signup
from .forms import (
    SignupForm,
    BookvehicleForm,
    ProceedForm,
    ContactForm,
    summaryForm,
    PaymentForm
)
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from v_trans import settings
from django.contrib.auth import authenticate
import random
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
def index(request):
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm.save()
            #useremail='sodvadiya789@gmail.com'
            #rec=[useremail,]
            #subject='Sing up success'
            #message="Your Singup success"
            #email_from=settings.EMAIL_HOST_USER
            #send_mail(subject,message,email_from,rec)
            print("sucessfully signup")
            return redirect('index2')
        else:
            print ('something went wrong.... in sign up')
    else:
        signupfrm=SignupForm()
    return render(request,'index.html',{'signupfrm':signupfrm})

def login(request):   
    if request.method=='POST':
        useremail=request.POST['useremail']
        userpassword=request.POST['userpassword']
        print(useremail,userpassword)
        try:
            user = signup.objects.get(emailid=useremail,password=userpassword)
            request.session['useremail']=user.emailid
            print("sucessfully Login with us!!!")
            return redirect('index2',{'useremail':useremail})
        except:
            return render(request,"index.html")
    else:
        return render(request,"index.html")

def logout(request):
    try:
        del request.session['useremail']
    except KeyError:
        pass
    return redirect("index")


def index2(request):
    return render(request,"index2.html",)
    

def vehicle(request):
    if request.session.has_key('useremail'):
    #book vehicle
        if request.method=='POST':
            bvehiclefrm=BookvehicleForm(request.POST)
            if bvehiclefrm.is_valid():
                bvehiclefrm.save()
                return redirect('checkfare')
                print('vehicle book successfully!!')
            else:
                print('something went wrong')
        else:
            bvehiclefrm=BookvehicleForm()
        return render(request,'vehicle.html',{'bvehiclefrm':bvehiclefrm})
    else:
        return redirect('/')
def services(request):
    return render(request,'services.html')

def about(request):
    if request.method=="POST":
        contactfrm=ContactForm(request.POST)
        if contactfrm.is_valid():
            contactfrm.save()
            print("submit successfully!!")
        else:
            print("something worng here..")
    else:
        contactfrm=ContactForm
    return render(request,'about.html',{'contactfrm':contactfrm})


def checkfare(request):
    if request.method=='POST':
        proceedfrm=ProceedForm(request.POST)
        if proceedfrm.is_valid():
            proceedfrm.save()
            return redirect('bookingsummary')
            print('book sucessfully!..')
        else:
            print('something went wrong')
    else:
        proceedfrm=ProceedForm()
    return render(request,'checkfare.html',{'proceedfrm':proceedfrm})


def bookingsummary(request):
    
        if request.method=='POST':
            
            summaryfrm=summaryForm(request.POST)
            
            if summaryfrm.is_valid():
                summaryfrm.save()
                return redirect('afterproceed')
            
                print("summary show sucessfully!")
            else:
                print("summary not showen something went wrong here...")
        else:
            summaryfrm=summaryForm()
        bookingdata = proceed.objects.all().order_by('-id')[:1]
        return render(request, 'bookingsummary.html',{'bookingdata':bookingdata})


def blog(request):
    return render(request,'blog.html')


def afterproceed(request):
    if request.method=='POST':
        paymentfrm=PaymentForm(request.POST)
        payment=random.randint(2000,5000)
        if paymentfrm.is_valid():
            paymentfrm.save()
            print("payment sucessfully done!!")
            return redirect('index2')
        else:
            print("payment not complated, something uncondtinaliy exception here...")
    else:
        paymentfrm=PaymentForm()
    return render(request,'afterproceed.html',{'paymentfrm':paymentfrm,'payment':payment})

def forgot(request):
    return render(request,'forgot.html')

def gallery(request):
    return render (request, 'gallery.html')