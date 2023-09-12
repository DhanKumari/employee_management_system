from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from poll.models import *

# Create your views here.

@login_required(login_url="/login/")
def index(request): # Request will be the default argument
    context={}
    questions = Question.objects.all()  
    context['title']='polls'  # {{title}} is a placeholder for a variable that will be provided when rendering the template.
    context['questions']=questions 
    return render(request, 'polls/index.html', context)

@login_required(login_url="/login/")
def details(request, id=None): 
    context={}
    try:
        question = Question.objects.get(id=id) 
    except:
        raise Http404 
    context['question']=question
    return render(request, 'polls/details.html', context)

@login_required(login_url="/login/")
def random(request, id=None):
    if request.method == "GET":
        
        try:
            question = Question.objects.get(id=id) 
        except:
            raise Http404 
        context={}
        context['question']=question

        return render(request, 'polls/random.html',context)
    if request.method =="POST":
        user_id =1
        print(request.POST)
        data = request.POST
        ret=Answer.objects.create(user_id=user_id, choice_id=data['choice']) #dict.
        if ret:
            return HttpResponse("your vote is done successfully")
        else:
            return HttpResponse("your vote is  not done")

