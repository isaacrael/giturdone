from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def git_quiz(request):
    return render(request, 'git_quiz.html')
