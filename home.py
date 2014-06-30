__author__ = 'ian'

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
#indexing now
#fdghj

def index(request):
    return render_to_response('index.html')
