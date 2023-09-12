from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.views.generic import DetailView, ListView
#from django.views.generic.edit import UpdateView
from django.urls import reverse
#from django.urls import reverse_lazy
from employee.forms import UserForm
#from ems.decorators import admin_hr_required, admin_only

# Create your views here.

def user_login(request):
    context={}
    if request.method=="POST":
        username =  request.POST['username']  
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # To check the data in database 
        if user:
            login(request, user) 
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success')) # It directs u to success page
        else:
           context["error"]="Provide valid credentials!! "
           return render(request, "auth/login.html",context)

    else:
        return render(request,"auth/login.html", context)
    

@login_required(login_url="/login/") 
def  success(request): # After successful login user becomes a parameter of request  
    context={}
    context['user']= request.user
    return render(request, "auth/success.html",context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")  # Restricts the user if they have not logged in 
def employee_list(request): # Request will be the default argument
    context={}
    context['users']=User.objects.all()  
    context['title']='Employees'
    return render(request, 'employee/index.html', context)

@login_required(login_url="/login/")
def employee_details(request, id=None): # Request will be the default argument
    context={}
    context['user']=get_object_or_404(User, id=id)  
    return render(request, 'employee/details.html', context)

@login_required(login_url="/login/")
def employee_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u=user_form.save()    
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html',context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'employee/add.html', context)

@login_required(login_url="/login/")
def employee_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()    
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'employee/edit.html', {"user_form": user_form})

def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)
