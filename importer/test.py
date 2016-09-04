import sys, os
path = "/Users/abhishekk/os_projects/django-mongo"
abs_path = os.path.abspath("../voterx_app")
sys.path.append(abs_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings

import ipdb; ipdb.set_trace()