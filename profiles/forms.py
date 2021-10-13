from django import forms
from django.utils.safestring import mark_safe
from string import Template
from .models import Profile


class PictureWidget(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None, *args, **kwargs):
        try:
            img_src = value.url
        except AttributeError:
            img_src = '/media/avatars/' + str(value) # TODO: There MUST be a better way to do this!
        img_html = mark_safe(f'<img id="current-avatar" class="avatar-sm" src="{img_src}"/>')
        input_html = super().render(name, value, attrs={'id': 'image-input'}, **kwargs)
        return f'{img_html}{input_html}'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
    avatar = forms.ImageField(widget=PictureWidget)