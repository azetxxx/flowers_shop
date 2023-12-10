# import os

# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowers_shop.settings')
# django.setup()

from .celery import app as celery_app

__all__ = ('celery_app',)
