#-*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from models import *

class news_list(ListView):
	model = News 
	template_name = 'cms/news_list.html'
