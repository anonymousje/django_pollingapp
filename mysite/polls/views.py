from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }

    return HttpResponse(template.render(context, request))
    #output = ', '.join([q.question_test for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello World. You're are the polls index")

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    
    
    #try:
     #   question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "you are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):

    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', { 'question' : question, 'error_message' : "you did not select a choice",})

    else: 
            selected_choice.votes +=1
            selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):

    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', { 'question' : question, 'error_message' : "you did not select a choice",})

    else: 
            selected_choice.votes +=1
            selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
 