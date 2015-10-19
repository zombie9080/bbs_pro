from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from models import *

# Create your views here.
def index(req):
	bbs = BBS.objects.all()
	t=get_template('home.html')
	c=RequestContext(req,locals())
	return HttpResponse(t.render(c))

def detail(req,id):
	bbs = BBS.objects.filter(id=int(id))[0]
	t = get_template('detail.html')
	c = RequestContext(req,locals())
	return HttpResponse(t.render(c))
