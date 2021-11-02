
from directmessages.models import Message
from directmessages.apps import Inbox
from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(label='Type your message below.', widget=forms.Textarea())
    def save(self, sender, recipient):
        Inbox.send_message(sender, recipient, self.cleaned_data['content'])