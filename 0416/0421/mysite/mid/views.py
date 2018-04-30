from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Introduce
# Create your views here.
def index(request):
	introduce=Introduce.objects.all()
	return render_to_response('myname.html', locals())