from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message

# Create your views here.

# @login_required
def messagebox_view(req):
    user = req.user
    inbox = Message.objects.all().filter(recipient=user)
    outbox = Message.objects.all().filter(sender=user)
    context = {
        'inbox': inbox,
        'outbox': outbox,
    }
    return render(req, 'messaging/messagebox.html', context)
