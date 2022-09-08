from django.apps import AppConfig
from django.http import HttpResponse,Http404

from django.contrib.auth.models import User


class BoardsConfig(AppConfig):
    name = 'boards'
