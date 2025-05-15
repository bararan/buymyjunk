from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Message, Thread
from .forms import MessageForm

# Create your views here.

@login_required
def messagebox_view(req):
    user = req.user
    inbox = Thread.objects.filter(users__in=[user]).all()
    # ReplyFormSet = inlineformset_factory(Thread, Message, form=MessageForm, extra=len(inbox))
    # threads_w_forms = []
    # for thread in inbox:
    #     threads_w_forms.append([thread, ReplyFormSet(req.POST,instance=thread)])
# TODO: The validation below is not correct. Think how to do it properly.
    msg_form = MessageForm(data=req.POST or None)
    active_thread = inbox[0]
    if req.method == 'POST':
        if msg_form.is_valid():
            message = message_form.save(commit=False)
            message.thread = thread
            reply = reply_form.save()
    context = {
        'username': user.username,
        'inbox': inbox,
        'active_thread': inbox[0] or None
        # 'reply_forms': reply_forms,
    }
    return render(req, 'messaging/messagebox.html', context)


# class MsgBoxView(ListView, LoginRequiredMixin):
#     template_name = 'messaging/messagebox.html'
#     model = Message

# def message_box_view(req):
#     return render(req, 'messaging/messagebox.html')