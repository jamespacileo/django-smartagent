from functools import wraps

from django.shortcuts import render_to_response
from django.http import HttpResponse

def render_to(template=None, mobile_template=None, mimetype=None):
    """
    Based upon django-annoying: https://bitbucket.org/offline/django-annoying/

    Decorator for Django views that sends returned dict to render_to_response 
    function.

    Template name can be decorator parameter or TEMPLATE item in returned 
    dictionary.  RequestContext always added as context instance.
    If view doesn't return dict then decorator simply returns output.

    Parameters:
     - template: template name to use
     - mobile_template: template used when device is mobile device
     - mimetype: content type to send in response headers
    """
    def renderer(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            if request.browser_data.get('ismobiledevice') and not request.session.get('force_desktop_version'):
                template = mobile_template
            tmpl = output.pop('TEMPLATE', template)
            return render_to_response(tmpl, output, \
                        context_instance=RequestContext(request), mimetype=mimetype)
        return wrapper
    return renderer