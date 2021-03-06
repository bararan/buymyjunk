from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileEditForm
# Create your views here.

# TODO: Below is a placeholder. Either replace or remove!
@login_required
def all_profiles_view(req):
    profiles = Profile.objects.all()
    for p in profiles:
        print(p.id, p)
    return HttpResponse()

@login_required
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
            if req.method == 'POST':
                confirmed = profile_form.is_valid()
                if confirmed:
                    profile_form.save()
                    messages.add_message(req, messages.SUCCESS, 'You have updated your profile.')
                else:
                    print('Errors:', profile_form.errors)
                    print('Non-field errors:', profile_form.non_field_errors)
    except Profile.DoesNotExist:
        # profile = None
        message = 'The requested profile could not be found.'
        messages.add_message(req, messages.WARNING, message)
        return HttpResponseRedirect('/')
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
