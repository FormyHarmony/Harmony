from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import Restaurnet,Food
def index(request):
		restaurents=Restaurnet.objects.all()
		return render_to_response('menu.html', locals())
