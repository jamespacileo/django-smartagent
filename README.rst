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
------

To install the app add ``django_smartagent`` to ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...
        'django_smartagent',
        ...
    )

Place ``agents.pk`` within the root of the project directory 

or alternatively set the AGENT_DATASET_LOCATION setting to the desired path for the agent data file.


Settings
------

A settings variable can be added to your project settings.

The structure is the following:

::

    SMART_AGENT_SETTINGS = {
        'AGENT_DATASET_LOCATION': 'agents.pk',
    }

Usage
------

django-smartagent adds the ``browser_data`` dictionary to the ``request`` object containing features associated with the user's browser.

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
