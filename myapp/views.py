from django.shortcuts import (
    render, 
    HttpResponse,
    redirect,
    #render_to_response
)

#models

from .models import (
    bookvehicle, 
    proceed,
    contactus,
    summary,
    payment,
)
from .models import signup

#forms

from .forms import (
    SignupForm,
    BookvehicleForm,
    ProceedForm,
    ContactForm,
    summaryForm,
    PaymentForm,
)

##others

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from v_trans import settings
from django.contrib.auth import authenticate
import random
from django.contrib import messages
from django.template import RequestContext

#paytm
from .models import Transaction
from .paytm import(
    generate_checksum,
    verify_checksum
)
from django.views.decorators.csrf import csrf_exempt

#shortcut

from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm.save()
            send_mail('Mail From V-Trans', 'Youre are Sucessfully Signup with us!!!','transv38@gmail.com',['dipsodvadiya112@gmail.com'])
            
            return redirect('index2')
            messages.info(request, 'You are sucessfully sign up with us!!!')
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
            return redirect('index2')
            messages.info(request, 'login Successfully!!!')
        except:
            messages.error(request, 'Please enter correct email or password')
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
    messages.info(request,'Your credentials is safe with us!!')
    return render(request,"index2.html")
    
@login_required
def vehicle(request):
    if request.session.has_key('useremail'):
        messages.error(request,'please login or singin')
    #book vehicle
        if request.method=='POST':
            bvehiclefrm=BookvehicleForm(request.POST)
            if bvehiclefrm.is_valid():
                bvehiclefrm.save()
                return redirect('checkfare')
                print('vehicle book successfully!!')
            else:
                print('something went wrong in Vehicle views')
        else:
            bvehiclefrm=BookvehicleForm()
            return render(request,'vehicle.html',{'bvehiclefrm':bvehiclefrm})
    else:
        print("Please Login First!!!!")
        messages.error(request,'Please register yourself first!!!!')
        return redirect('index')

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


@login_required
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
    bookingdata = proceed.objects.all().order_by('-id')[:1]
    return render(request,'checkfare.html',{'proceedfrm':proceedfrm})

@login_required
def bookingsummary(request):
        if request.method=='POST':
            summaryfrm=summaryForm(request.POST)
            #payment1=random.randint(2000,5000)
            if summaryfrm.is_valid():
                summaryfrm.save()
                return redirect('afterproceed')
                print("summary show sucessfully!")
            else:
                print("summary not showen something went wrong here...")
        else:
            summaryfrm=summaryForm()
        bookingdata = proceed.objects.all().order_by('-id')[:1]
        return render(request, 'bookingsummary.html',{'bookingdata':bookingdata,'summaryfrm':summaryfrm})


def blog(request):
    return render(request,'blog.html')

def gallery(request):
    return render (request, 'gallery.html')

def faq(request):
    return render(request,'faq.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def payterms(request):
    return render(request, 'payterms.html')


#paytm 

def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'pay.html')
    try:
       
        amount = int(request.POST['amount'])
       
    except:
        return render(request, 'pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create( amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str("dipsodvadiya112@gmail.com")),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            messages.info(request, 'Your Booking successfully!!')
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'callback.html', context=received_data)
        return render(request, 'callback.html', context=received_data)