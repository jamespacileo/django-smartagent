from django.test import TestCase

from smartagent.utils import detect_user_agent

class BrowserDetectionTest(TestCase):

    def test_user_agent_recognition(self):

        user_agent_list = {
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5":{
                'platform': 'iPhone OSX',
            }
        }

        for user_agent, user_agent_meta in user_agent_list.items():
            result = detect_user_agent(user_agent)
            self.assertEqual(result['platform'], user_agent_meta['platform'])

        

