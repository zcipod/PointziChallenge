import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'


def before_all(context):
    django.setup()



