from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileEditForm
# Create your views here.

# TODO: Below is a placeholder. Either replace or remove!
def all_profiles_view(req):
    profiles = Profile.objects.all()
    for p in profiles:
        print(p.id, p)
    return HttpResponse()

def profile_view(req, pk):
    profile_form = None
    try:
        profile =Profile.objects.get(id=int(pk))
        is_own = req.user == profile.user
        if is_own:
            profile_form = ProfileEditForm(
                req.POST or None,
                req.FILES or None,
                instance=profile
            )
            confirmed = profile_form.is_valid()
            if confirmed:
                profile_form.save()
            else:
                print('Errors:', profile_form.errors)
                print(dir(profile_form.non_field_errors))
    except Profile.DoesNotExist:
        profile = None
    context = {
        'object':profile,
        # 'is_own': is_own,
        'profile_form': profile_form,
    }
    return render(req, 'profiles/view.html', context)

# TODO: This is redundant. Delete
# def update_profile_view(req):
#     if req.is_ajax:
#         bio = req.POST.get('bio')
#         avatar = req.POST.get('avatar')
#         print(avatar)
#         profile = Profile.objects.get(user = req.user)
#         print(profile)
#         profile.save()
#         return HttpResponse()
