from ConfigParser import SafeConfigParser
import cPickle as pickle
from copy import copy
import time
import re
import os

from django.conf import settings
from django.core.cache import cache

CACHE_KEY = 'agents.pk'
CACHE_TIME = 60*60*24  # daily

SMART_AGENT_SETTINGS = {
    'AGENT_DATASET_LOCATION': 'agents.pk',
}

if hasattr(settings, 'SMART_AGENT_SETTINGS'):
    SMART_AGENT_SETTINGS.update(settings.SMART_AGENT_SETTINGS)

agents = cache.get(CACHE_KEY, [])
if not agents:
    agents = pickle.load(open(SMART_AGENT_SETTINGS['AGENT_DATASET_LOCATION'], 'rb'))
    cache.set(CACHE_KEY, agents, CACHE_TIME)

#try:
#    agents = pickle.load(open('useragent_detector/agents.pk', 'rb'))
#except IOError:
#    pythonize_browscap(write_to_file='agents.pk')

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
    candidates = []
    for agent in agents:
        if agent['regex'].match(user_agent_string):
            candidates.append(agent)

    start = time.time()
    candidates.sort(key=lambda x: x['depth'])

    start = time.time()
    result = get_user_agent_characteristics(candidates[-1])
    return result

if __name__=="__main__":
    ua = "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5"
    print detect_user_agent(ua)
