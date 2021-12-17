import os
import celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')

app = celery.Celery(
    'portfolio_backend',
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()