from django import forms
from .models import Item, Image

class PostItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('seller',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('item',)

ImageFormSet = forms.modelformset_factory(Image, form=ImageForm, extra=4, max_num=4)
''' TODO: In the image formset prevent multiple images from being marked as main image and
    disable is_main checkbox for fields without uploaded images.
    TODO: Make it possible to delete images in this form.
'''