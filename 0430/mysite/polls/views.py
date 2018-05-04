
from django.http import HttpResponse
from .models import  Question
from django.shortcuts import  render

def search_form(request):
    return render(request, 'mother.html')

def search(request):
    request.encoding = 'utf-8'
    message = 'What you fill in is: ' + request.GET.get('q')
    r2 = Question.objects.create(question_text = request.GET.get('q'))
    return HttpResponse(message)


