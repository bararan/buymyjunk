from django import forms
from .models import Message, Thread

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # exclude = ('thread', 'sender', 'recipient')
        fields = ('content',)

    def print_data(self):
        print(self.cleaned_data)

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('subject',)