import os, sys

sys.path.append('C:/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'testserver.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()