# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response


def browser_data(request):
    return render_to_response('browser_data.html', {'browser_data': request.browser_data}, context_instance=RequestContext(request))


