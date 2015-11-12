from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . models import Answer, Question
import random
import datetime
from django.utils.encoding import *

# Create your views here.

# This context processor function takes the request
# object and returns a dictionary of context variables
# to be made available to all templates.

def get_current_time(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  context = {}
  context['current_time'] = datetime.datetime.now()
  return context



def index(request):
    return render(request, 'index.html')

"""
def git_quiz(request):
    questions = list(Question.objects.all())
    question = random.shuffle(questions)
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': questions}
#    questions = list(question_answer.keys())
#    question = random.choice(questions)
    return render(request, 'giturdone_quiz/index.html', context)
"""


def git_quiz(request):
    latest_question_list = Question.objects.all()[:9]
#    latest_question_list = random.shuffle(temp_latest_question_list)
    context = {'latest_question_list': latest_question_list}
#    questions = list(question_answer.keys())
#    question = random.choice(questions)
    return render(request, 'giturdone_quiz/index.html', context)





def git_resources(request):
        return render(request, 'giturdone_quiz/resources.html')





def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'giturdone_quiz/detail.html', {'question': question})


def answer(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question answer form.
        return render(request, 'giturdone_quiz/detail.html', {
            'question': p,
            'error_message': "You didn't select an answer.",
        })
    else:
        selected_choice.answers += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('giturdone_quiz:results', args=(p.id,)))



"""
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'giturdone_quiz/results.html', {'question': question})
"""


def results(request, question_id):
    latest_question_list = Question.objects.order_by('?')[:2]

    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        user_answer = request.POST.get('textfield', None)
        # Get the question object
        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
        a = q.answer_set.all()
        # Get the first element in the list of answers
        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
        correct_answer = smart_text(value)
        context = {'latest_question_list': latest_question_list, 'answer': user_answer, 'question': question, 'correct_answer': correct_answer}
        value = "gil"
    return render(request, 'giturdone_quiz/results.html', context)


"""
def results(request):
    if request.method == 'POST':
        user_answer = request.POST.get('textfield', None)
        value = "gil"
    return render(request, 'giturdone_quiz/results.html', {'answer': user_answer})
"""

