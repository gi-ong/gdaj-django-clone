from django.shortcuts import render
from django.views.generic import DetailView
from . import models


class PageView(DetailView):

    """ PageView Definition """
    model = models.Page
