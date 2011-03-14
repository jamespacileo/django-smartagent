from django_smartagent.utils import detect_user_agent

NEEDED_VALUES = set(['browser', 'majorver', 'minorver', 'cookies',
'activexcontrols', 'cdf', 'parent_index', 'supportscss', 'aolversion',
'frames', 'cssversion', 'isbanned', 'tables', 'iframes', 'vbscript',
'ismobiledevice', 'platform', 'version', 'aol', 'javaapplets', 'parent',
'backgroundsounds', 'win64', 'javascript', 'beta', 'alpha',
'issyndicationreader', 'win32', 'depth', 'crawler', 'win16'])

class UserAgentDetectorMiddleware(object):

    def process_request(self, request):
        """
        Add browser features to request object
        """
        _user_agent = request.META['HTTP_USER_AGENT']
        _user_agent = detect_user_agent(_user_agent)
        user_agent = _user_agent.copy()

        keys = user_agent.keys()
        for key in keys:
            if key not in NEEDED_VALUES:
                user_agent.pop(key)
        request.browser_data = user_agent
