# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntrySection'
        db.create_table(u'blog_entrysection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assets_from_images', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Entry'])),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_caption', self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['EntrySection'])


        # Changing field 'Entry.date_modified'
        db.alter_column(u'blog_entry', 'date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

    def backwards(self, orm):
        # Deleting model 'EntrySection'
        db.delete_table(u'blog_entrysection')


        # Changing field 'Entry.date_modified'
        db.alter_column(u'blog_entry', 'date_modified', self.gf('django.db.models.fields.DateTimeField')(null=True))

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
            'assets_from_images': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'draft_file': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'external_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        },
        u'blog.entrysection': {
            'Meta': {'ordering': "['entry', 'index']", 'object_name': 'EntrySection'},
            'assets_from_images': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_caption': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']