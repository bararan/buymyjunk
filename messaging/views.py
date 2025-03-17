from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Message, Thread

# Create your views here.

@login_required
def messagebox_view(req):
    user = req.user
    inbox = Message.objects.filter(recipient=user).all() # TODO: Does this work?? if not try User.
    for c in inbox:
        print(c)
    outbox = Message.objects.all().filter(sender=user)
    context = {
        'inbox': inbox,
        'outbox': outbox,
    }
    return render(req, 'messaging/messagebox.html', context)
    # TODO: Change this view to accommodate Thread model. In list view all threads should be collapsed with subject and usernames visible.
    #       Once the thread is expanded individual messages should become visible.


class MsgBoxView(ListView, LoginRequiredMixin):
    template_name = 'messaging/messagebox.html'
    model = Message

# def message_box_view(req):
#     return render(req, 'messaging/messagebox.html')