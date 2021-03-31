def index(request):

    #signup
    if request.method=='POST':
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm.save()
            #email=SignupForm.cleaned_data.get('email')
            return redirect('index2')
            #sending mail
            #send_mail('Re:Singup succesfully', 'You are sucessfully registered with us!! Enjoy our services..',settings.EMAIL_HOST_USER,['dipsodvadiya789@gmail.com','manitbabariya1999@gmail.com'])
            email_subject = 'V-Trans',
            email_body = 'You`re suceesfully sign up with us, enjou=y our services',
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                request.POST['emailid'],
                fail_silently=False,
            )
            print("sucessfully signup")

        #login
        #elif request.method=='POST':

            #email=request.POST['emailid']
            #pas=request.POST['password']

            #login_check=authenticate(emailid=email, password=pas)
            #login_check=signup.objects.filter(emailid=email, password=pas)
            #login_check=signup.objects.filter(emailid=email, password=pas)

            #if login_check:
               
               # print('login successfully!!!')
               # return redirect('index2')
            #else:
               # print('error.... Invalid login')

        #else:
            #print(signupfrm.errors)
    else:
        signupfrm=SignupForm()
    return render(request,'index.html',{'signupfrm':signupfrm})

#def login(request):
  # s=signup.objects.filter(emailid=request.POST['e_id'],password=request.POST['password'])
    #if s:
      #  request.session['useremail']=request.POST["emailid"]
      #  return redirect("index2")
  #  else:
       # return render(request,"index.html",{'Error':'Invalid Userid and Password '})

def login(request):
    
    if request.POST.get('login')=='login':
        uemail=request.POST['emailid']
        pas=request.POST['password']

        stid=signup.objects.get(emailid=uemail)

        user=signup.objects.filter(emailid=uemail,password=pas)
        print(stid,user)
        if user:
            request.session['userid']=uemail
            request.session['stid']=stid.id
            print('Login Successfully!')
            return redirect('index2')
        else:
            print('Error...Invalid User!')
    else:
        return render(request,"index.html")



# tops code 
def index(request):  
     if request.method=='POST':
        if request.POST.get('login')=='login':
            email=request.POST['emailid']
            pas=request.POST['password']

            stid=signup.objects.get(emailid=email)

            user=signup.objects.filter(emailid=email,password=pas)
            if user:
                request.session['userid']=email
                request.session['stid']=stid.id
                print('Login Successfully!')
                return redirect('index2')
            else:
                print('Error...Invalid User!')
        elif request.POST.get('signup')=='signup':
            signupfrm=SignupForm(request.POST)
            if signupfrm.is_valid():
                signupfrm.save()
                print("Signup Successfully!")
                return redirect('index2')
            else:
                print(signupfrm.errors)
    else:
        signupfrm=SignupForm()
    return render(request,'index.html',{'signupfrm':signupfrm})