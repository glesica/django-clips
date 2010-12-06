from django.db import models

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from taggit.managers import TaggableManager
from taggit.models import Tag, GenericTaggedItemBase


class ClipTag(Tag):
    """
    A clip tag that includes a description of the tag.
    """
    description = models.TextField(
        blank=True,
        null=True,
    )


class TaggedClip(GenericTaggedItemBase):
    """
    Through model for custom tag.
    """
    tag = models.ForeignKey(ClipTag)


class Clip(TimeStampedModel):
    """
    Movie or episode snippet.
    
    Automatically has: created, modified
    """
    name = models.CharField(max_length=250)
    description = models.TextField()
    source = models.ForeignKey(
        'ClipSource',
        blank=True,
        null=True,
    )
    icon = models.ImageField(
        upload_to='uploads/clip-icons/',
        blank=True,
        null=True,
    )
    season_number = models.IntegerField(
        blank=True,
        null=True,
    )
    disc_number = models.IntegerField(
        blank=True,
        null=True,
    )
    segments = models.ManyToManyField(
        'ClipSegment',
        blank=True,
        null=True,
    )
    credit = models.ForeignKey(
        'Contributor',
        blank=True,
        null=True,
    )
    embed_id = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-modified', 'name']
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('clips.views.clip', (), {'clip_id': self.id})
    
    def get_avg_rating(self):
        return self.ratings.aggregate(models.Avg('score'))


class ClipSource(TitleSlugDescriptionModel):
    """
    A television show that has been cataloged.
    
    Automatically has: title, slug, description.
    """
    source_type = models.CharField(
        max_length=250,
        choices=(('m', 'Movie'), ('t', 'Television Show'), ('c', 'Commerical')),
    )
    
    class Meta:
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        #TODO fix this to use url lookup
        return '/yadadb/%s/' % self.slug


class ClipSegment(models.Model):
    """
    A time segment within a clip.
    """
    start_hours = models.IntegerField()
    start_minutes = models.IntegerField()
    start_seconds = models.IntegerField()
    end_hours = models.IntegerField()
    end_minutes = models.IntegerField()
    end_seconds = models.IntegerField()

    def __unicode__(self):
        return '%s - %s' % (self.start_text(), self.end_text())
    
    class Meta:
        ordering = ['start_hours', 'start_minutes', 'start_seconds']
    
    def start_text(self):
        return '%02i:%02i:%02i' % (self.start_hours, self.start_minutes, self.start_seconds)
    
    def end_text(self):
        return '%02i:%02i:%02i' % (self.end_hours, self.end_minutes, self.end_seconds)
    
    def start_in_seconds(self):
        start = self.start_seconds + self.start_minutes * 60 + self.start_hours * 60 * 60
        return start
    
    def end_in_seconds(self):
        end = self.end_seconds + self.end_minutes * 60 + self.end_hours *60 * 60
        return end
    
    def length_in_seconds(self):
        length = self.end_in_seconds - self.start_in_seconds
        return length


class Contributor(models.Model):
    """
    A person who contributed a clip.
    """
    first_name = models.CharField(max_length=250)    
    last_name = models.CharField(max_length=250)
    institution = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        ordering = ['last_name']
