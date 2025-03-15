from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    subject = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='threads', related_query_name='thread')

    def get_users(self):
        return self.users

    def __str__(self):
        parties = self.get_users()
        return f'Conversation between users {parties[0]} and {parties[1]}'


# TODO: Should the thread also have an 'unread' indicator?
# TODO: Thread's read/unread status should depend on who receives the message. Pay attention!
class Message(models.Model):
    sender =models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='recipient')
    subject = models.CharField(max_length=120, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE) 
    content = models.TextField(max_length=500)
    # unread = models.BinaryField(default=True) # This should not be at this level, needs to be user specific.
    sent_at = models.DateTimeField(auto_now_add=True)
    # readable_by = models.ManyToManyField(User) # This should 
    # TODO: Think about what should happen when the foreign keys are deleted!

    def mark_as_read(self):
        self.unread = False

    def mark_as_unread(self):
        self.unread = True
    
    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username} on {self.sent_at}'
    
    

