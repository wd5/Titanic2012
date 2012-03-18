# -*- coding: utf-8 -*-
from datetime import datetime

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from forum.models import Thread, Comment
from forum.forms import ThreadForm, CommentForm


def render_to_response(request, template_name, context_dict=None):
    from django.shortcuts import render_to_response as _render_to_response
    context = RequestContext(request, context_dict or {})
    return _render_to_response(template_name, context_instance=context)


def index(request):
    if request.POST and request.user.is_authenticated():
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('forum_index'))
    else:
        form = ThreadForm()

    return render_to_response(request, 'forum/index.html',
            {'threads': Thread.objects.all().order_by('-last_comment_date'),
             'user': request.user.is_authenticated() and request.user or None,
             'form': form,
        })


def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.POST and request.user.is_authenticated():
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(thread, request.user)
            thread.last_comment_date = datetime.now()
            thread.save()
            return HttpResponseRedirect(reverse('forum_thread', args=[thread_id]))
    else:
        form = CommentForm()

    return render_to_response(request, 'forum/thread.html',
            {'thread': thread,
             'user': request.user.is_authenticated() and request.user or None,
             'comments': Comment.objects.filter(thread=thread).order_by('date_created'),
             'form': form,
        })


def edit_comment(request, comment_id):
    pass
