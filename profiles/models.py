from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    bio = models.TextField(default='Introduce yourself.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_items_for_sale(self):
        from items.models import Item
        return Item.objects.filter(seller = self)

    def __str__(self):
        return f"{self.user.username}'s profile"
