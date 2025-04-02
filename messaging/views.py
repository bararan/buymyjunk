from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Message, Thread
from .forms import MessageForm
from django.forms import inlineformset_factory

# Create your views here.

@login_required
def messagebox_view(req):
    user = req.user
    inbox = Thread.objects.filter(users__in=[user]).all()
    ReplyFormSet = inlineformset_factory(Thread, Message, form=MessageForm, extra=len(inbox))
    threads_w_forms = []
    for thread in inbox:
        threads_w_forms.append([thread, ReplyFormSet(req.POST,instance=thread)])
# TODO: The validation below is not correct. Think how to do it properly.
    if req.method == 'POST':
        if reply_form.is_valid():
            reply.thread = thread
            reply = reply_form.save()
    context = {
        'username': user.username,
        'inbox': threads_w_forms,
        # 'reply_forms': reply_forms,
    }
    return render(req, 'messaging/messagebox.html', context)


# class MsgBoxView(ListView, LoginRequiredMixin):
#     template_name = 'messaging/messagebox.html'
#     model = Message

# def message_box_view(req):
#     return render(req, 'messaging/messagebox.html')