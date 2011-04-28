from django.http import HttpResponseRedirect

def force_desktop_version(request):
    """
    Adds a session variable marking if the user wishes to view the desktop version
    """
    request.session['force_desktop_version'] = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def unforce_desktop_version(request):
    """
    Adds a session variable marking if the user does not wish to view the desktop version
    """
    request.session['force_desktop_version'] = False
    return HttpResponseRedirect(request.META['HTTP_REFERER'])