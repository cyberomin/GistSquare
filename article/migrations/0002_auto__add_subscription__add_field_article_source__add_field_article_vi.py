# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscription'
        db.create_table(u'article_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'article', ['Subscription'])

        # Adding field 'Article.source'
        db.add_column(u'article_article', 'source',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Article.views'
        db.add_column(u'article_article', 'views',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Article.title'
        db.alter_column(u'article_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=400))

    def backwards(self, orm):
        # Deleting model 'Subscription'
        db.delete_table(u'article_subscription')

        # Deleting field 'Article.source'
        db.delete_column(u'article_article', 'source')

        # Deleting field 'Article.views'
        db.delete_column(u'article_article', 'views')


        # Changing field 'Article.title'
        db.alter_column(u'article_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'article.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['article']