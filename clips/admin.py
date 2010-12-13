from django.contrib import admin

from clips.models import ClipTag, Clip, ClipSegment, ClipSource, Contributor

admin.site.register(Clip)
admin.site.register(ClipSegment)
admin.site.register(ClipSource)
admin.site.register(Contributor)
admin.site.register(ClipTag)
