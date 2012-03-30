# -*- coding: utf-8 -*-
from datetime import datetime
from django import forms
from forum.models import Thread, Comment


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': 60}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 12}))

    def save(self, user):
        thread = Thread(title=self.cleaned_data['title'], last_comment_date=datetime.now())
        thread.save()
        comment = Comment(author=user, thread=thread, content=self.cleaned_data['content'])
        comment.save()


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 12}))

    def save(self, thread, user):
        comment = Comment(author=user, thread=thread, content=self.cleaned_data['content'])
        comment.save()
