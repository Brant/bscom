# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Entry.category'
        db.alter_column(u'blog_entry', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'], null=True))

    def backwards(self, orm):

        # Changing field 'Entry.category'
        db.alter_column(u'blog_entry', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['blog.Category']))

    models = {
        u'blog.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'default_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        },
        u'blog.entry': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Entry'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'external_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        }
    }

    complete_apps = ['blog']