from useragent_detector.utils import detect_user_agent

class UserAgentDetectorMiddleware(object):

    def process_request(self, request):
        """
        Add browser features to request object
        """
        user_agent = request.META['HTTP_USER_AGENT']
        print user_agent
        user_agent = detect_user_agent(user_agent)

        request.is_mobile = False
        if user_agent.has_key('ismobiledevice'):
            if user_agent['ismobiledevice'] in ['true', True]:
                request.is_mobile = True
        
        if request.GET.has_key('mobile'):
            request.is_mobile = True
