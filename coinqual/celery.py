from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinqual.settings')

app = Celery('coinqual')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings',namespace='CELERY')



# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from celery.schedules import crontab
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'priceupdate0',
        'schedule': 180.0,
    },
    '1hour-30min-tokenrefreshin':{
     'task': 'token_refresh0',
     'schedule':5400.0,
    },
}



#app.conf.beat_schedule = {
#    '1hour-30min-tokenrefreshin': {
#        'task': 'token_refresh0',
#        'schedule': 5100.0,
#    },
#}


#yes




