from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login,logout
from .models import CustomUser,Staffs,Students,AdminHOD
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def loginUser(request):
    return render(request,'login_page.html')

def doLogin(request):
    email_id=request.GET.get('email')
    password=request.GET.get("password")

    if not (email_id and password):
        messages.error(request,'please provide the details')
        return render(request,'login_page.html')
    user=CustomUser.objects.filter(email=email_id).last()
    if not user or not check_password(password,user.password):
        messages.error(request,'Invalid Login Credintials')
        return render(request,'login_page.html')

    login(request,user)

    if user.user_type==CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type==CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type==CustomUser.HOD:
        return redirect('admin_home/')
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def doRegistration(request):
    first_name=request.GET.get('first_name')
    last_name=request.GET.get('lastname')
    email_id=request.GET.get('email')
    password=request.GET.get('password')
    confirm_password=request.GET.get('confirmPassword')

    if not (email_id and password and confirm_password):
        messages.error(request,'please provide all the details')
        return render(request,'registration.html')
    if password!=confirm_password:
        messages.error(request,'Both passwords should match')
        return render(request,'registration.html')
    if CustomUser.objects.filter(email=email_id).exits():
        messages.error(request,'User with this email already exists. Please login')
        return render(request,'registration.html')
    user_type=get_user_type_from_email(email_id)

    if user_type is None:
        messages.error(request,"Email must be like: 'ram.student@college.com','sita.staff@institute.edu or 'principal.hod@university.org'")
    username=email_id.split('@')[0].split('.')[0]

    if CustomUser.objects.filter(username=username).exists():
        messages.error(request,'User with this username already exists.Please choose a different email')
        return render(request,'registration.html')
    
    user=CustomUser()
    user.username=username
    user.email=email_id
    user.first_name=first_name
    user.last_name=last_name
    user.user_type=user_type
    user.set_password(password)
    user.save()

    if user_type==CustomUser.STAFF:
        Staffs.objects.create(admin=user)
    elif user_type==CustomUser.STUDENT:
        Students.objects.create(admin=user)
    elif user_type==CustomUser.HOD:
        AdminHOD.objects.create(admin=user)

    messages.success(request,'Registration successful.Please logg in')
    return render(request,'login_page.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def get_user_type_from_email(email_id):
    try:
        email_user_type=email_id.split('@')[0].split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        return None
    

