from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . models import Answer, Question
import random


# Create your views here.


def index(request):
    return render(request, 'index.html')


def git_quiz(request):
    questions = Question.objects.all()[:5]
    question = random.choice(questions)
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': questions}
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


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'giturdone_quiz/results.html', {'question': question})

