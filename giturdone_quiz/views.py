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
# TODO add a button that allows computer user to zero out their scores
# TODO add functionality that zeros out scores on logout


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


# git_quiz displays the quiz selected by user in the Quiz Selection page

def git_quiz(request):
    if user_response == 'None':
        return render(request, 'giturdone_quiz/index.html')
    if user_response == '1':
        latest_question_list = Question.objects.filter(category="Git Basics")
    if user_response == '2':
        latest_question_list = Question.objects.filter(category="Git Undoing Changes")
    if user_response == '3':
        latest_question_list = Question.objects.filter(category="Git Rewriting History")
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


def results(request, question_id):
    latest_question_list = Question.objects.order_by('?')
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        selected_answer = Answer.objects.get(pk=question_id)
        # Gets my_answer -> the answer associated with question_id
        my_answer = Answer.objects.filter(question_id=question_id)
        # Get the image "post_image/filename" for my_answer
        for item in my_answer:
            image = item.image
        image=str(item.image)

        # Concatenates "/media/" + "post_image/filename"
        image=("/media/" + (image))
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
        # initialize variables
        sum = 0
        total_correct_answers=0
        ttl_correct = 0
        ttl_c = 0
        total_wrong_answers = 0
        ttl_wrong = 0
        ttl_w = 0
        ttl_questions_answered = 0
        score = 0
        Grade = str("")
        # if correct answer increment total_correct_answers by 1 for the selected answer
        if correct_answer == user_answer:
            selected_answer.total_correct_answers += 1
            selected_answer.save()
        else:
        # if wrong answer increment total_wrong_answers by for the selected answer
            selected_answer.total_wrong_answers += 1
            selected_answer.save()
        # add up all the total_correct_answers -> produces a dictionary
        ttl_correct = Answer.objects.aggregate(Sum('total_correct_answers'))
        # assign the dictionary value to ttl_c
        ttl_c = (ttl_correct["total_correct_answers__sum"])
        # add up all the total_wrong_answers -> produces a dictionary
        ttl_wrong = Answer.objects.aggregate(Sum('total_wrong_answers'))
        # assign the dictionary value to ttl_w
        ttl_w = (ttl_wrong["total_wrong_answers__sum"])
        # calculate total questions answered
        ttl_questions_answered = ttl_c + ttl_w
        # calculate quiz score
        score = (float(ttl_c)/float(ttl_questions_answered) * 100)
        # make score and integer so that if elif statements below handle the score value correctly
        score = round(int(score), 2)
        if score in range(90,101):
            Grade = "A"
        elif score in range(80,90):
            Grade = "B"
        elif score in range(70,80):
            Grade = "C"
        elif score in range(60,70):
            Grade = "D"
        elif score in range(0,59):
            Grade = "F"
        context = {'latest_question_list': latest_question_list, 'answer': user_answer,
        'question': question, 'correct_answer': correct_answer, 'Grade':Grade,
        'score':score, 'total_questions_answered': ttl_questions_answered,
        'total_correct_answers': ttl_c, 'total_wrong_answers': ttl_w, 'image': image}
    return render(request, 'giturdone_quiz/results.html', context)


def reset_scores(request):
    answer_item = 0
    answers = Answer.objects.all()
    for answer_item in answers:
        answer_item.total_correct_answers = 0
        answer_item.total_wrong_answers = 0
        answer_item.save()
    return render(request, 'giturdone_quiz/reset_scores.html')

def short_answer_quiz_categories(request):
    if request.method == 'POST':
        return render(request, 'giturdone_quiz/index.html')
    else:
        return render(request, 'giturdone_quiz/short_answer_quiz_categories.html')


def tools(request):
    return render(request, 'giturdone_quiz/tools.html')



def feynman_technique_quiz(request):
    return render(request, 'giturdone_quiz/feynman_technique_quiz.html')


def multiple_choice_quiz(request):
    return render(request, 'giturdone_quiz/multiple_choice_quiz.html')