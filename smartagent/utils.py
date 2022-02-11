from ConfigParser import SafeConfigParser
import cPickle as pickle
from copy import copy
import time
import re
import os

from django.conf import settings

APP_DIRNAME = os.path.abspath(os.path.dirname(__file__))

SMART_AGENT_SETTINGS = {
    'AGENT_DATASET_LOCATION': os.path.join(APP_DIRNAME, 'agents_basic.pkl'),
}

if hasattr(settings, 'SMART_AGENT_SETTINGS'):
    SMART_AGENT_SETTINGS.update(settings.SMART_AGENT_SETTINGS)

AGENT_DATASET_LOCATION = SMART_AGENT_SETTINGS['AGENT_DATASET_LOCATION']

try:
    agents = pickle.load(open(AGENT_DATASET_LOCATION, 'rb'))
except TypeError:
    raise Warning("User-Agent dataset cannot be found! Make sure that AGENT_DATASET_LOCATION is set.")

def load_agents():
    agents = pickle.load(open(SMART_AGENT_SETTINGS['AGENT_DATASET_LOCATION'], 'rb'))

def get_user_agent_characteristics(agent):
    """
    Get UserAgent's feature list
    """
    current_agent = agent
    while current_agent.has_key('parent'):
        index = current_agent['parent_index']
        parent = agents[index]
        current_agent = parent
        parent_copy = copy(parent)
        parent_copy.update(agent)
        agent = parent_copy
    return agent

def detect_user_agent(user_agent_string):
    """
    >>> r = detect_user_agent("Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5")
    >>> r['platform'] == 'iPhone OSX'
    True
    """

    start = time.time()
    candidates = [
        agent for agent in agents if agent['regex'].match(user_agent_string)
    ]

    start = time.time()
    candidates.sort(key=lambda x: len(x['name']))

    start = time.time()
    return get_user_agent_characteristics(candidates[-1])

def all_possible_matches(user_agent_string):
    candidates = [
        agent for agent in agents if agent['regex'].match(user_agent_string)
    ]

    candidates.sort(key=lambda x: len(x['name']))
    return [(item['name'], item['depth']) for item in candidates]

if __name__=="__main__":
    ua = "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5"
    print detect_user_agent(ua)['ismobiledevice']

    ua = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16"
    print detect_user_agent(ua)['browser']

    ua = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0"
    print detect_user_agent(ua)['browser']