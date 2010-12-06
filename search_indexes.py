from haystack import indexes, site

from clips.models import Clip, ClipSource

class ClipIndex(indexes.SearchIndex):
    text = indexes.CharField(
        document=True,
        use_template=True,
    )
    
    def get_queryset(self):
        """
        This is in place until the site moves beyond Seinfeld. Filters clips
        for only Seinfeld so database can be updated with additional sources
        that will stay hidden.
        """
        source = ClipSource.objects.get(slug='seinfeld')
        return Clip.objects.filter(source=source)

site.register(Clip, ClipIndex)
