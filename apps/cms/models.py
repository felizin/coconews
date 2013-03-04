#-*- coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Author(models.Model):
	name = models.CharField(_('Name'), max_length=30)

class Categories(models.Model):
	category = models.CharField(_('Category'), max_length=30)

	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')
	def __unicode__(self):
		return self.category

class News(models.Model):
    title = models.CharField(_('Title'), max_length=60)
    author = models.ManyToManyField(Author, verbose_name=_('Author'))
    categories = models.ManyToManyField(_('Categories'))
    editor = models.ForeignKey(User, verbose_name=_('Editor'))
    CONTENT_TYPE_CHOICES = (
    	('general', _('General')),
    	('markdown', _('Markdown')),
    	('gallery', _('Gallery')),
    )
    content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, default='general', max_length=10, verbose_name=_('Content type'))
    STATUS_CHOICES = (
    	('editing', _('Editing')),
    	('published', _('published')),
    	('deleted', _('Deleted')),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='editing', max_length=15, verbose_name=_('Status'))
    date_modify = models.DateField(_('Date'), auto_now=True)
    date_publish = models.DateField(_('Date'), auto_now_add=True)

    class Meta:
    	verbose_name = _('News')
    	verbose_name_plural = _('News')
    def __unicode__(self):
    	return self.title

class Tags(models.Model):
	tag = models.CharField(_('Tag'), max_length=15)
	news = models.ManyToManyField(News, verbose_name=_('News'))

	class Meta:
		verbose_name=_('Tag')
		verbose_name_plural = _('Tags')
	def __unicode__(self):
		return self.tag

    



