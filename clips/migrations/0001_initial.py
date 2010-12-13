# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ClipTag'
        db.create_table('clips_cliptag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('clips', ['ClipTag'])

        # Adding model 'TaggedClip'
        db.create_table('clips_taggedclip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clips_taggedclip_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clips_taggedclip_items', to=orm['clips.ClipTag'])),
        ))
        db.send_create_signal('clips', ['TaggedClip'])

        # Adding model 'Clip'
        db.create_table('clips_clip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clips.ClipSource'], null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('season_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('disc_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('credit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clips.Contributor'], null=True, blank=True)),
            ('embed_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('clips', ['Clip'])

        # Adding M2M table for field segments on 'Clip'
        db.create_table('clips_clip_segments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['clips.clip'], null=False)),
            ('clipsegment', models.ForeignKey(orm['clips.clipsegment'], null=False))
        ))
        db.create_unique('clips_clip_segments', ['clip_id', 'clipsegment_id'])

        # Adding model 'ClipSource'
        db.create_table('clips_clipsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source_type', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('clips', ['ClipSource'])

        # Adding model 'ClipSegment'
        db.create_table('clips_clipsegment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_hours', self.gf('django.db.models.fields.IntegerField')()),
            ('start_minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('start_seconds', self.gf('django.db.models.fields.IntegerField')()),
            ('end_hours', self.gf('django.db.models.fields.IntegerField')()),
            ('end_minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('end_seconds', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('clips', ['ClipSegment'])

        # Adding model 'Contributor'
        db.create_table('clips_contributor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('clips', ['Contributor'])


    def backwards(self, orm):
        
        # Deleting model 'ClipTag'
        db.delete_table('clips_cliptag')

        # Deleting model 'TaggedClip'
        db.delete_table('clips_taggedclip')

        # Deleting model 'Clip'
        db.delete_table('clips_clip')

        # Removing M2M table for field segments on 'Clip'
        db.delete_table('clips_clip_segments')

        # Deleting model 'ClipSource'
        db.delete_table('clips_clipsource')

        # Deleting model 'ClipSegment'
        db.delete_table('clips_clipsegment')

        # Deleting model 'Contributor'
        db.delete_table('clips_contributor')


    models = {
        'clips.clip': {
            'Meta': {'ordering': "['-modified', 'name']", 'object_name': 'Clip'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'credit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clips.Contributor']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'disc_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'embed_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'season_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'segments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clips.ClipSegment']", 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clips.ClipSource']", 'null': 'True', 'blank': 'True'})
        },
        'clips.clipsegment': {
            'Meta': {'ordering': "['start_hours', 'start_minutes', 'start_seconds']", 'object_name': 'ClipSegment'},
            'end_hours': ('django.db.models.fields.IntegerField', [], {}),
            'end_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'end_seconds': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_hours': ('django.db.models.fields.IntegerField', [], {}),
            'start_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'start_seconds': ('django.db.models.fields.IntegerField', [], {})
        },
        'clips.clipsource': {
            'Meta': {'ordering': "['title']", 'object_name': 'ClipSource'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'source_type': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'clips.cliptag': {
            'Meta': {'object_name': 'ClipTag'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'clips.contributor': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Contributor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'clips.taggedclip': {
            'Meta': {'object_name': 'TaggedClip'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clips_taggedclip_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clips_taggedclip_items'", 'to': "orm['clips.ClipTag']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['clips']
