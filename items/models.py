from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from profiles.models import Profile


# Create your models here.

class Item(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(default='Enter item description', max_length=5000)
    price = models.FloatField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_images(self):
        return Image.objects.filter(item=self)

    def get_main_image(self):
        try:
            img = Image.objects.get(item=self, is_main=True).image
            return img
        except Image.DoesNotExist:
            try:
                # If no image is marked as main image return the first image for the item
                return Image.objects.filter(item=self).first().image
            except AttributeError:
                return None

    def get_absolute_url(self):
        return reverse("items:details", kwargs={"pk": self.pk})

    def get_deletion_url(self):
        return reverse("items:delete", kwargs={"pk": self.pk})


    def __str__(self):
        return f"{self.title}. Price: {self.price:.2f} by {self.seller.user.username}"


class Image(models.Model):
    image = models.ImageField(upload_to='items')
    is_main = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     other_imgs = Image.objects.filter(
    #         item=self.item
    #     )
    #     if len(other_imgs) == 0:
    #         self.is_main = True # if it's the first image for this item automatically make it the main image.
    #     return super().save(*args, **kwargs)

    ''' Decided it would be better to do this through views'''
    # def make_main_image(self, *args, **kwargs):
    #     prev_main = Image.objects.get(item=self.item, is_main=True) # Find the previous main 
    #     print(f"Found {prev_main}")
    #     if prev_main:
    #         prev_main.is_main = False # Unset it as the main image
    #         prev_main.save()
    #     self.main_image = True
    #     print(prev_main)
    #     print(self)
    #     self.save(*args, **kwargs) # Do we need args&kwargs here??

    def __str__(self):
        return f"Main image for {self.item.title}" if self.is_main else f"Image for {self.item.title}."
