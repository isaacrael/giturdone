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
# The line below imports the user_response variable from the user_response.py file
from . user_response import user_response
from processors import custom_processor
from django.db.models import Sum

# TODO add comments to this module



# Create your views here.



# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')

# quiz_selection page takes a user_response as input and displays associated quiz on Sensei Quiz page

def quiz_selection(request):
    if request.method == 'POST':
        user_response = request.POST.get('textfield', None)
        user_response = smart_text(user_response)
        f = open('giturdone_quiz/user_response.py', 'w')
        # the line below write the text 'user_response = ' and concats the user_response the str function gets rid of u in front of string
        f.write('user_response = ' + repr(str(user_response)))
        f.close()
    return render(request, 'giturdone_quiz/quiz_selection.html')


# git_quiz displays the quiz selected by user in the Sensei Quiz Selection page

def git_quiz(request):
    if user_response == 'None':
        return render(request, 'giturdone_quiz/index.html')
    if user_response == '1':
        latest_question_list = Question.objects.filter(category="Git Basics")
    if user_response == '2':
        latest_question_list = Question.objects.filter(category="Git Undoing Changes")
    if user_response == '3':
        latest_question_list = Question.objects.filter(category="Git Rewriting Git History")
    if user_response == '4':
        latest_question_list = Question.objects.filter(category="Git Branches")
    if user_response == '5':
        latest_question_list = Question.objects.filter(category="Git Remote Repositories")
    if user_response == '6':
        latest_question_list = Question.objects.filter(category="Git Config")
    if user_response == '7':
        latest_question_list = Question.objects.filter(category="Git Log")
    if user_response == '8':
        latest_question_list = Question.objects.filter(category="Git Diff")
    if user_response == '9':
        latest_question_list = Question.objects.filter(category="Git Reset")
    if user_response == '10':
        latest_question_list = Question.objects.filter(category="Git Rebase")
    if user_response == '11':
        latest_question_list = Question.objects.filter(category="Git Pull")
    if user_response == '12':
        latest_question_list = Question.objects.filter(category="Git Push")
    context = {'user_response': user_response, 'latest_question_list': latest_question_list}
    return render(request, 'giturdone_quiz/index.html', context)


def git_resources(request):
        return render(request, 'giturdone_quiz/resources.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'giturdone_quiz/detail.html', {'question': question})

"""
# Note: The answer function below is not being used but is left here
# as an example for future versions of the application and may be able
# to be used to implement a way to show a computer users test score based
# on the number of questions answered correctly vs. total questions responded to

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
    latest_question_list = Question.objects.order_by('?')
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        selected_answer = Answer.objects.get(pk=question_id)
        user_answer = request.POST.get('textfield', None)
        # Get the question object
        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
        a = q.answer_set.all()
        # Get the first element in the list of answers
        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
        correct_answer = smart_text(value)
        # code for score calculator
        sum = 0
        total_correct_answers=0
        ttl_correct = 0
        ttl_c = 0
        total_wrong_answers = 0
        ttl_wrong = 0
        ttl_w = 0
        ttl_questions_answered = 0
        score = 0
        Grade = str("text")
        if correct_answer == user_answer:
            selected_answer.total_correct_answers += 1
            selected_answer.save()
        else:
            selected_answer.total_wrong_answers += 1
            selected_answer.save()
        ttl_correct = Answer.objects.aggregate(Sum('total_correct_answers'))
        ttl_c = (ttl_correct["total_correct_answers__sum"])
        ttl_wrong = Answer.objects.aggregate(Sum('total_wrong_answers'))
        ttl_w = (ttl_wrong["total_wrong_answers__sum"])
        ttl_questions_answered = ttl_c + ttl_w
        score = (float(ttl_c)/float(ttl_questions_answered) * 100)
        score = round(score, 2)
        if score in range(90,100):
            Grade = "A"
        elif score in range(80,90):
            Grade = "B"
        elif score in range(70,80):
            Grade = "C"
        elif score in range(60,70):
            Grade = "D"
        elif score in range(50,60):
            Grade = "F"


        context = {'latest_question_list': latest_question_list, 'answer': user_answer,
        'question': question, 'correct_answer': correct_answer, 'Grade':Grade, 'score':score, 'total_questions_answered': ttl_questions_answered, 'total_correct_answers': ttl_c, 'total_wrong_answers': ttl_w}
    return render(request, 'giturdone_quiz/results.html', context)



