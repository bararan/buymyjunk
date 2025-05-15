from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    subject = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='threads', related_query_name='thread')
    subject = models.CharField(max_length=120, null=True)

    @property
    def get_users(self):
        return list(self.users.all())

    @property
    def messages(self):
        return Message.objects.filter(thread=self)

    def __str__(self):
        parties = self.get_users
        return f"Conversation between users {' and '.join([p.username for p in parties])}"


# TODO: Should I move subject to Thread?
class Message(models.Model):
    sender =models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='recipient')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE) 
    content = models.TextField(max_length=500)
    # unread = models.BinaryField(default=True) # This should not be at this level, needs to be user specific.
    sent_at = models.DateTimeField(auto_now_add=True)
    # readable_by = models.ManyToManyField(User) # This should 
    # TODO: Think about what should happen when the foreign keys are deleted!
    # def save(self, thread=None, subject=None):
    #     if thread is None:
    #         thread = Thread.objects.create(subject=subject)
    #         thread.users.add(self.sender, self.recipient)
    #         thread.save()
    #     self.thread = thread
    #     super().save()

    def mark_as_read(self):
        self.unread = False

    def mark_as_unread(self):
        self.unread = True
    
    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username} on {self.sent_at}'
    
    

