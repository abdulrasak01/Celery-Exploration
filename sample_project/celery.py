from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_project.settings')

app = Celery('sample_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Check if the environment is Windows and set 'solo' pool to avoid multiprocessing issues
if os.name == 'nt':  # If the OS is Windows
    app.conf.update(
        worker_pool='solo',  # Use solo pool for Windows to avoid multiprocessing issues
    )

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
