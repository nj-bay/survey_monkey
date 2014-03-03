# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.author'
        db.delete_column(u'survey_question', 'author_id')

        # Deleting field 'Question.quest'
        db.delete_column(u'survey_question', 'quest')

        # Deleting field 'Question.posted'
        db.delete_column(u'survey_question', 'posted')

        # Adding field 'Question.survey'
        db.add_column(u'survey_question', 'survey',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['survey.Survey']),
                      keep_default=False)

        # Adding field 'Question.question'
        db.add_column(u'survey_question', 'question',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Survey.author'
        db.delete_column(u'survey_survey', 'author_id')

        # Deleting field 'Survey.question'
        db.delete_column(u'survey_survey', 'question_id')

        # Deleting field 'Survey.posted'
        db.delete_column(u'survey_survey', 'posted')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Question.author'
        raise RuntimeError("Cannot reverse this migration. 'Question.author' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Question.author'
        db.add_column(u'survey_question', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Question.quest'
        raise RuntimeError("Cannot reverse this migration. 'Question.quest' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Question.quest'
        db.add_column(u'survey_question', 'quest',
                      self.gf('django.db.models.fields.CharField')(max_length=500),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Question.posted'
        raise RuntimeError("Cannot reverse this migration. 'Question.posted' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Question.posted'
        db.add_column(u'survey_question', 'posted',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'Question.survey'
        db.delete_column(u'survey_question', 'survey_id')

        # Deleting field 'Question.question'
        db.delete_column(u'survey_question', 'question')


        # User chose to not deal with backwards NULL issues for 'Survey.author'
        raise RuntimeError("Cannot reverse this migration. 'Survey.author' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Survey.author'
        db.add_column(u'survey_survey', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Survey.question'
        raise RuntimeError("Cannot reverse this migration. 'Survey.question' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Survey.question'
        db.add_column(u'survey_survey', 'question',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Question']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Survey.posted'
        raise RuntimeError("Cannot reverse this migration. 'Survey.posted' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Survey.posted'
        db.add_column(u'survey_survey', 'posted',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True),
                      keep_default=False)


    models = {
        u'survey.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['survey']