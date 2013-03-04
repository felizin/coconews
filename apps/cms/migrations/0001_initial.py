# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('cms_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('cms', ['Author'])

        # Adding model 'Categories'
        db.create_table('cms_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('cms', ['Categories'])

        # Adding model 'News'
        db.create_table('cms_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('editor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.CharField')(default='general', max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(default='editing', max_length=15)),
            ('date_modify', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date_publish', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['News'])

        # Adding M2M table for field author on 'News'
        db.create_table('cms_news_author', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news', models.ForeignKey(orm['cms.news'], null=False)),
            ('author', models.ForeignKey(orm['cms.author'], null=False))
        ))
        db.create_unique('cms_news_author', ['news_id', 'author_id'])

        # Adding M2M table for field categories on 'News'
        db.create_table('cms_news_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news', models.ForeignKey(orm['cms.news'], null=False)),
            ('categories', models.ForeignKey(orm['cms.categories'], null=False))
        ))
        db.create_unique('cms_news_categories', ['news_id', 'categories_id'])

        # Adding model 'Tags'
        db.create_table('cms_tags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('cms', ['Tags'])

        # Adding M2M table for field news on 'Tags'
        db.create_table('cms_tags_news', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tags', models.ForeignKey(orm['cms.tags'], null=False)),
            ('news', models.ForeignKey(orm['cms.news'], null=False))
        ))
        db.create_unique('cms_tags_news', ['tags_id', 'news_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('cms_author')

        # Deleting model 'Categories'
        db.delete_table('cms_categories')

        # Deleting model 'News'
        db.delete_table('cms_news')

        # Removing M2M table for field author on 'News'
        db.delete_table('cms_news_author')

        # Removing M2M table for field categories on 'News'
        db.delete_table('cms_news_categories')

        # Deleting model 'Tags'
        db.delete_table('cms_tags')

        # Removing M2M table for field news on 'Tags'
        db.delete_table('cms_tags_news')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'cms.categories': {
            'Meta': {'object_name': 'Categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cms.news': {
            'Meta': {'object_name': 'News'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Author']", 'symmetrical': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Categories']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'general'", 'max_length': '10'}),
            'date_modify': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_publish': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'editing'", 'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'cms.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.News']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cms']