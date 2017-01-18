from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.db.models import Q

@login_required(login_url='/')
def home(request):
	context = {}
	return render(request,'core/home.html',context)
	
def index(request):
	if request.user.is_authenticated:
		return redirect('core:home')
	return render(request, 'core/index.html')

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		if User.objects.filter(username=username).exists():
			return render(request, 'core/index.html',{'error' : "Username already exists, login or choose another one!"})
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('core:home'))	
	return HttpResponseRedirect(reverse('core:index'))

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('core:home'))
		return render(request, 'core/index.html',{'error' : "Wrong username or password!"})
	return HttpResponseRedirect(reverse('core:index'))

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))




