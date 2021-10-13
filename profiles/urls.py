from django.urls import path
from .views import profile_view, all_profiles_view#, update_profile_view

app_name = 'profiles'

urlpatterns = [
    path('', all_profiles_view, name='allprofs'),
    # path('update/', update_profile_view, name='update'),
    path('<pk>', profile_view, name='profile'),
]
