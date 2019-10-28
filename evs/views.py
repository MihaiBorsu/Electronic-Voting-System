from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404,render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('evs/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def home(request):
    return HttpResponse("Home page")

def voting_event_detail(request, votingevent_id):
    voting_event = get_object_or_404()
    return HttpResponse("You're looking at voting event number: %s." % votingevent_id)

def question_detail(request, question_id, votingevent_id):  # voting event id to be added
    return HttpResponse("You're looking at question number: %s in the voting event number %s." % (question_id,votingevent_id))

def result(request, question_id, votingevent_id): # voting event id to be added
    response = "You're looking at the result of the question: %s that is part of the voting event %s."
    return HttpResponse(response % (question_id,votingevent_id))

def vote (request, question_id, votingevent_id):  # voting event id to be added
    return HttpResponse("You're voting at question number %s, part of the voting event %s." % (question_id,votingevent_id))

# Create your views here.
