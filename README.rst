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


Installation
------

To install the app add ``django_smartagent`` to ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...
        'django_smartagent',
        ...
    )


Usage
------

django-smartagent adds the ``browser_data`` dictionary to the ``request`` object containing features associated with the user's browser.

Features available within the ``browser_Data`` dictionary

browser:
    Browser's name

majorver:
    Major version

minorver:
    Minor version

cookies:
    If cookies are supported

activexcontrols:
    If activexcontrols are supported

cdf:
    If Channel Definition Format is supported

supportscss:
    If CSS is supported

cssversion:
    Max CSS version supported

aolversion:
    Version

frames:
   If frames are supported

isbanned:
    

tables:
    If tables are supported

iframes:
    ...

vbscript:
    If browser supports Visaul Basic scripting

ismobiledevice:
    If host machine is a mobile device

platform:
    Host platform of the user's browser

version:
    Host OS version

aol:
    ...

javaapplets:
    If browser supports Java Applets

backgroundsounds:
    If browser supports background sounds

win64:
    If the host OS is 64bit

javascript:
    If browser supports Javascript

beta:
    If browser is a beta distribution

alpha:
    If browser is an alpha distribution

issyndicationreader:
    If user agent is a syndacation reader

win32:
    If the host OS is 32bit

crawler:
    If user agent is a web crawler

win16:
    If the host OS is 16bit
