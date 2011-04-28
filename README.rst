======
Django-SmartAgent
======
Description
------

:Author:
    James Pacileo

:Version:
    0.1.0

:Description:
    django-smartagent is an attempt to provide Django developers with a lightning fast and complete browser detection utility.

:Requirements:
    Django 1.2+

Installation
------------

To install the app add ``smartagent`` to ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...
        'smartagent',
        ...
    )

Add the middleware

::

    MIDDLEWARE_CLASSES = (
        ...
        'smartagent.middleware.UserAgentDetectorMiddleware',
    )

**The middleware** is used to attach the browser characteristics to the request object, which will be accessible through **request.browser_info**

User-Agent data file
----------------------------

Django-SmartAgent comes pre-packaged with a data file containing browser info **agents_basic.pkl**. The datafile is built using various resources on the net and generated to be made compatible with the library.

You can grab the latest datafile from github https://github.com/jamespacileo/django-smartagent/downloads.

Once you grab the latest data file, place it under your project folder. To inform Django-SmartAgent of the file location you need to edit settings.py by adding:

::

    SMART_AGENT_SETTINGS = {
        'AGENT_DATASET_LOCATION': '/path/to/agent_data_set.pkl',
    }

Utilities for mobile sites
--------------------------

As it is popular for sites to have a mobile version, there are a few utility methods within the project.

A **render_to** decorator (based on django-annoying's render_to) renders a page using a desktop or mobile version of a site, depending if the user-agent is a mobile device or not.

::

    @render_to(template='desktop_template.html', mobile_template='mobile_template.html')
    def page(request):

        articles = Articles.objects.all()[:30]
        return {
            'articles': articles,
        }

which is the equivalent of:

::

    def page(request):

        articles = Articles.objects.all()[:30]
        if request.browser_info.get('ismobiledevice') and not request.session.get('force_desktop_version'):
            return render_to_response('mobile_tempalte.html', {'articles':articles, },
                                                               context_instance=RequestContext(request))
        return render_to_response('desktop_tempalte.html', {'articles':articles, },
                                                            context_instance=RequestContext(request))


Two utility URLs exist which are used to force/unforce the desktop vesion of the site. This is due to users not always wanting to view the mobile version of the site.

- **smartagent/force_desktop_version/** forces the desktop version for mobile sites

- **smartagent/unforce_desktop_version** unforces the desktop version, forcing mobile devices to view the mobile version

::

    urlpatterns = patterns('',
        ...
        (r'^smartagent/', include('smartagent.urls')))

Settings
--------

A settings variable can be added to your project settings.

The structure is the following:

::

    SMART_AGENT_SETTINGS = {
        'AGENT_DATASET_LOCATION': 'agents.pk',
    }

Usage
-----

django-smartagent adds the ``browser_info`` dictionary to the ``request`` object containing features associated with the user's browser.

+-----------------------+----------------------------------------------+
+  Fields exposed within ``browser_data``                              +
+=======================+==============================================+
+  FIELD NAME           +  FIELD DESCRIPTION                           +
+-----------------------+----------------------------------------------+
+  cdf                  +  If Channel Definition Format is supported   +
+-----------------------+----------------------------------------------+
+  activexcontrols      +  If activexcontrols are supported            +
+-----------------------+----------------------------------------------+
+  cookies              +  If cookies are supported                    +
+-----------------------+----------------------------------------------+
+  supportscss          +  If CSS is supported                         +
+-----------------------+----------------------------------------------+
+  cssversion           +  Max CSS version supported                   +
+-----------------------+----------------------------------------------+
+  majorver             +  Major version                               +
+-----------------------+----------------------------------------------+
+  tables               +  If tables are supported                     +
+-----------------------+----------------------------------------------+
+  iframes              +  If iframes are supported                    +
+-----------------------+----------------------------------------------+
+  vbscript             +  If browser supports Visaul Basic scripting  +
+-----------------------+----------------------------------------------+
+  platform             +  Host platform of the user's browser         +
+-----------------------+----------------------------------------------+
+  version              +  Host OS version                             +
+-----------------------+----------------------------------------------+
+  javaapplets          +  If browser supports Java Applets            +
+-----------------------+----------------------------------------------+
+  backgroundsounds     +  If browser supports background sounds       +
+-----------------------+----------------------------------------------+
+  win64                +  If the host OS is 64bit                     +
+-----------------------+----------------------------------------------+
+  javascript           +  If browser supports Javascript              +
+-----------------------+----------------------------------------------+
+  beta                 +  If browser is a beta distribution           +
+-----------------------+----------------------------------------------+
+  alpha                +  If browser is an alpha distribution         +
+-----------------------+----------------------------------------------+
+  minorver             +  Minor version                               +
+-----------------------+----------------------------------------------+
+  issyndicationreader  +  If user agent is a syndacation reader       +
+-----------------------+----------------------------------------------+
+  win32                +  If the host OS is 32bit                     +
+-----------------------+----------------------------------------------+
+  ismobiledevice       +  If host machine is a mobile device          +
+-----------------------+----------------------------------------------+
+  crawler              +  If user agent is a web crawler              +
+-----------------------+----------------------------------------------+
+  win16                +  If the host OS is 16bit                     +
+-----------------------+----------------------------------------------+
+  browser              +  Browser's name                              +
+-----------------------+----------------------------------------------+
