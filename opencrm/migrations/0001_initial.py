# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('opencrm_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crm_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('birth_city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opencrm.City'])),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('crm_vat_registration_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('crm_social_security_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('legal_form', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bank_branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opencrm.Bank_branch'])),
            ('checking_account', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('checking_account_control', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('iban', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('legal_rep_firstname', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('legal_rep_lastname', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('identity_doc_number', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('identity_doc_date', self.gf('django.db.models.fields.DateField')()),
            ('identity_doc_city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opencrm.City'], null=True, related_name='identity_doc_city', blank=True)),
            ('headquarter_address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('headquarter_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True)),
            ('headquarter_postcode', self.gf('django.db.models.fields.CharField')(blank=True, max_length=10, null=True)),
            ('company_type', self.gf('django.db.models.fields.CharField')(blank=True, max_length=40, null=True)),
        ))
        db.send_create_signal('opencrm', ['Account'])

        # Adding model 'Bank_branch'
        db.create_table('opencrm_bank_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opencrm.Bank'])),
            ('bank_branch', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bank_brach_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('opencrm', ['Bank_branch'])

        # Adding model 'Bank'
        db.create_table('opencrm_bank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bank_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('opencrm', ['Bank'])

        # Adding model 'City'
        db.create_table('opencrm_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('municipality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('district', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
        ))
        db.send_create_signal('opencrm', ['City'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('opencrm_account')

        # Deleting model 'Bank_branch'
        db.delete_table('opencrm_bank_branch')

        # Deleting model 'Bank'
        db.delete_table('opencrm_bank')

        # Deleting model 'City'
        db.delete_table('opencrm_city')


    models = {
        'opencrm.account': {
            'Meta': {'object_name': 'Account'},
            'bank_branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opencrm.Bank_branch']"}),
            'birth_city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opencrm.City']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'checking_account': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'checking_account_control': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'company_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '40', 'null': 'True'}),
            'crm_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'crm_social_security_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'crm_vat_registration_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headquarter_address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'headquarter_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'headquarter_postcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'iban': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity_doc_city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opencrm.City']", 'null': 'True', 'related_name': "'identity_doc_city'", 'blank': 'True'}),
            'identity_doc_date': ('django.db.models.fields.DateField', [], {}),
            'identity_doc_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'legal_form': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'legal_rep_firstname': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'legal_rep_lastname': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'opencrm.bank': {
            'Meta': {'object_name': 'Bank'},
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bank_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'opencrm.bank_branch': {
            'Meta': {'object_name': 'Bank_branch'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opencrm.Bank']"}),
            'bank_brach_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bank_branch': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'opencrm.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['opencrm']