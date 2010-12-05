import csv

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from taggit.models import Tag

from clips.models import Clip, ClipTag
from clips.forms import RatingForm, PerPageForm
from clips.utils import paginate_clips

def clip_list(request, source_slug='seinfeld', tag_slug=None, home=False):
    """
    Main page.
    NOTE: source_slug defaults to 'seinfeld' until site moves over to 
    all pop culture, then should default to None
    """
    context = {}
    
    if 'page' not in request.GET or request.GET['page'] is not '1':
        context.update({
            'home': home,
        })
    
    # filter by source first
    if source_slug:
        clips = Clip.objects.filter(source__slug=source_slug)
    else:
        clips = Clip.objects.all()
    
    # then filter by tag name if necessary
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        context.update({
            'tag': tag,
        })
        clips = clips.filter(tags=tag)
    
    context.update(paginate_clips(clips, request))

    return render_to_response(
        'clips/index.html',
        context,
        context_instance=RequestContext(request)
    )

def tag_list(request):
    """
    Creates a list of all available tags. Used to create the index page.
    """
    context = {}
    
    tags = Tag.objects.all()
    
    context.update({
        'tags': tags,
    })
    
    return render_to_response(
        'clips/tags.html',
        context,
        context_instance=RequestContext(request)
    )

def clip(request, clip_id):
    """
    Single-clip view.
    """
    context = {}
    
    clip = get_object_or_404(Clip, pk=clip_id)
    
    # ratings
    if 'score' in request.GET:
        ratingform = RatingForm(request.GET)
        cliprating, new = ClipRating(clip=clip)
        if ratingform.is_valid():
            cliprating.score = ratingform.cleaned_data['score']
            cliprating.save()
            return redirect(clip)
    
    #TODO this needs to be adjusted to use the session instead of the db
    # Construct the rating list, 0 or 1 depending on star status
    #try:
    #    r = clip.ratings.get(user=request.user).score
    #except ClipRating.DoesNotExist:
    #    r = 0
    #clip.rating = [1]*r + [0]*(5-r) # this is magic to create a list like [1,1,0,0,0] (2 stars)
    
    context.update({
        'clip': clip,
    })
    
    return render_to_response(
        'clips/clip.html',
        context,
        context_instance=RequestContext(request)
    )

