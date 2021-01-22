from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .serializer import ProfileSerializer
from .forms import *
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only
import requests
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 
from django.core.mail import EmailMessage, send_mail
import requests  
# Create your views here.
def indexPage (request):
    title =" Home Page"
    context = {
        'title':title
    }
    return render(request, 'home.html',context)

@unauthenticated_user
def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            form = form.cleaned_data.get('email')
            subject="Thank you for Registering with Us "
            message ="Thank you for registering with InterIntel Technologies"
            email = EmailMessage(subject, message, to=[form])
            email.send()
            messages.success(request, 'Account for' + ' ' + username + 'was created successfully!!')
            return redirect('login')
        else:
            messages.error(request, 'Error creating the account. check if all the fields were correct and try again')
            return redirect('signup')
    else:
        form = RegisterForm()
    context = {
        'form':form
        }        
    return render(request, 'registration/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged in as' + ' ' + username)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
    context={}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have logged out. Thank you for using our services.')
    return redirect('index')

@login_required(login_url='login')
def profile(request, username):
    title ="Profile Page"
    profile_details =User.objects.get(username=username)
    try :
        profile_detail = Profile.get_by_id(profile_details.id)
    except:
        profile_detail = Profile.filter_by_id(profile_details.id)
     
    context ={
        'profile_details':profile_details,
        'profile_detail':profile_detail,
        'title':title
       
    }
    return render(request, 'profile/profile.html',context)

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)