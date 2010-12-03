"""
Utility functions for clips app.
"""

from django.core.paginator import Paginator, InvalidPage
from django.conf import settings
from clips.forms import PerPageForm

def paginate_clips(clips, request):
    """
    Paginate a set of clips and return the first page along with
    the number per page as a context dictionary.
    @param objects: a list of objects or a queryset to paginate
    @param get: a request associated with the page being generated
    """
     # determine which page we want
    if 'page' in request.GET:
        try:
            page = int(request.GET['page'])
        except ValueError:
            page = 1
    else:
        page = 1
    
    # determine how many we want on the page
    perpage = settings.CLIPS_DEFAULT_PER_PAGE
    if 'perpage' in request.GET:
        pageform = PerPageForm(request.GET)
        if pageform.is_valid():
            perpage = pageform.cleaned_data['perpage']
    
    # paginate
    paginator = Paginator(clips, perpage)
    try:
        clips = paginator.page(page)
    except InvalidPage:
        clips = paginator.page(paginator.num_pages)
    
    return {
        'page': page,
        'perpage': perpage,
        'clips': clips,
    }
