from django.conf.urls import url, patterns
from views import *
urlpatterns = patterns('',
	url(r'^$', news_list.as_view(), name='news_list'),
)